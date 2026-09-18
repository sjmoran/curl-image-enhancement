# -*- coding: utf-8 -*-
"""The CURL network: a TED backbone followed by the neural curve layer.

The loss lives in :mod:`losses` and the convolutional blocks in :mod:`blocks`.
``CURLLoss`` is re-exported here so that ``model.CURLLoss`` keeps working.
"""
import torch
import torch.nn as nn

import rgb_ted
from blocks import Block, ConvBlock, GlobalPoolingBlock, MaxPoolBlock
from colour import hsv_to_rgb, lab_to_rgb, rgb_to_hsv, rgb_to_lab
from curves import adjust_hsv, adjust_lab, adjust_rgb
from losses import CURLLoss

__all__ = ['CURLNet', 'CURLLayer', 'CURLLoss', 'Block', 'ConvBlock',
           'MaxPoolBlock', 'GlobalPoolingBlock']


class CURLLayer(nn.Module):

    #: Each colour stage: the conversion in, the curve application, the
    #: conversion out, and how many head outputs it consumes.
    STAGES = {
        'lab': (rgb_to_lab, adjust_lab, lab_to_rgb, 48),
        'rgb': (None, adjust_rgb, None, 48),
        'hsv': (rgb_to_hsv, adjust_hsv, hsv_to_rgb, 64),
    }

    def __init__(self, num_in_channels=64, num_out_channels=64,
                 colour_order=('lab', 'rgb', 'hsv')):
        """Initialisation of class

        :param num_in_channels: number of input channels
        :param num_out_channels: number of output channels
        :param colour_order: the colour spaces the block applies, in order.
            The default is the paper's LAB->RGB->HSV. A shorter tuple drops
            the spaces it omits, which is the Table II ablation; a different
            ordering is the Table III ablation.
        :returns: N/A
        :rtype: N/A

        """
        super(CURLLayer, self).__init__()

        unknown = [c for c in colour_order if c not in self.STAGES]
        if unknown:
            raise ValueError('unknown colour space(s): %s' % unknown)
        if not colour_order:
            raise ValueError('colour_order needs at least one colour space')
        self.colour_order = tuple(colour_order)

        self.num_in_channels = num_in_channels
        self.num_out_channels = num_out_channels
        self.make_init_network()

    def make_init_network(self):
        """ Initialise the CURL block layers

        :returns: N/A
        :rtype: N/A

        """
        self.lab_layer1 = ConvBlock(64, 64)
        self.lab_layer2 = MaxPoolBlock()
        self.lab_layer3 = ConvBlock(64, 64)
        self.lab_layer4 = MaxPoolBlock()
        self.lab_layer5 = ConvBlock(64, 64)
        self.lab_layer6 = MaxPoolBlock()
        self.lab_layer7 = ConvBlock(64, 64)
        self.lab_layer8 = GlobalPoolingBlock()

        self.fc_lab = torch.nn.Linear(64, 48)

        self.dropout1 = nn.Dropout(0.5)
        self.dropout2 = nn.Dropout(0.5)
        self.dropout3 = nn.Dropout(0.5)

        self.rgb_layer1 = ConvBlock(64, 64)
        self.rgb_layer2 = MaxPoolBlock()
        self.rgb_layer3 = ConvBlock(64, 64)
        self.rgb_layer4 = MaxPoolBlock()
        self.rgb_layer5 = ConvBlock(64, 64)
        self.rgb_layer6 = MaxPoolBlock()
        self.rgb_layer7 = ConvBlock(64, 64)
        self.rgb_layer8 = GlobalPoolingBlock()

        self.fc_rgb = torch.nn.Linear(64, 48)

        self.hsv_layer1 = ConvBlock(64, 64)
        self.hsv_layer2 = MaxPoolBlock()
        self.hsv_layer3 = ConvBlock(64, 64)
        self.hsv_layer4 = MaxPoolBlock()
        self.hsv_layer5 = ConvBlock(64, 64)
        self.hsv_layer6 = MaxPoolBlock()
        self.hsv_layer7 = ConvBlock(64, 64)
        self.hsv_layer8 = GlobalPoolingBlock()

        self.fc_hsv = torch.nn.Linear(64, 64)

    def _head(self, prefix, feat_img, dropout):
        """The eight-block head for one colour space, and its linear layer."""
        x = feat_img
        for i in range(1, 9):
            x = getattr(self, '%s_layer%d' % (prefix, i))(x)
        x = x.view(x.size()[0], -1)
        x = dropout(x)
        return getattr(self, 'fc_%s' % prefix)(x)

    def forward(self, x):
        """Forward function for the CURL layer

        :param x: forward the data x through the network
        :returns: Tensor representing the predicted image
        :rtype: Tensor

        """

        '''
        This function is where the magic happens :)
        '''
        x.contiguous()  # remove memory holes

        feat = x[:, 3:64, :, :]
        img = x[:, 0:3, :, :]

        dropouts = {'lab': self.dropout1, 'rgb': self.dropout2,
                    'hsv': self.dropout3}

        # The block builds a residual: each stage converts the running image
        # into its colour space, applies the curves its head predicts, and
        # converts back, so the stages compose in the order given.
        current = torch.clamp(img, 0, 1)
        gradient_regulariser = 0

        for space in self.colour_order:
            to_space, adjust, from_space, n_out = self.STAGES[space]
            if to_space is not None:
                current = torch.clamp(to_space(current), 0, 1)
            params = self._head(space, torch.cat((feat, current), 1),
                                dropouts[space])
            current, reg = adjust(current, params[:, 0:n_out])
            current = torch.clamp(current, 0, 1)
            if from_space is not None:
                current = torch.clamp(from_space(current), 0, 1)
            gradient_regulariser = gradient_regulariser + reg

        img = torch.clamp(img + current, 0, 1)

        return img, gradient_regulariser


class CURLNet(nn.Module):

    def __init__(self, msca_every_level: bool = False,
                 colour_order=('lab', 'rgb', 'hsv')):
        """Initialisation function

        :returns: initialises parameters of the neural networ
        :rtype: N/A

        """
        super(CURLNet, self).__init__()
        self.tednet = rgb_ted.TEDModel(msca_every_level=msca_every_level)
        self.curllayer = CURLLayer(colour_order=colour_order)

    def forward(self, img):
        """Neural network forward function

        :param img: forward the data img through the network
        :returns: residual image
        :rtype: numpy ndarray

        """
        feat = self.tednet(img)
        img, gradient_regulariser = self.curllayer(feat)
        return img, gradient_regulariser
