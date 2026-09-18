# -*- coding: utf-8 -*-
"""Device selection: CUDA if present, then Apple Silicon (MPS), then CPU.

The original code called ``.cuda()`` directly, so it ran only on an NVIDIA GPU.
Everything now goes through ``DEVICE``.
"""
import torch


def _pick():
    if torch.cuda.is_available():
        return torch.device('cuda')
    if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        return torch.device('mps')
    return torch.device('cpu')


DEVICE = _pick()


def empty_cache():
    """Free cached GPU memory, where the backend has a cache to free."""
    if DEVICE.type == 'cuda':
        torch.cuda.empty_cache()
