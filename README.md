# CURL: Neural Curve Layers for Global Image Enhancement (ICPR 2020)

[Sean Moran](http://www.seanjmoran.com),  Steven McDonagh, [Greg Slabaugh](http://gregslabaugh.net/)

Repository links for the paper CURL: Neural Curve Layers for Global Image Enhancement. Here you will find a link to the code and information of the datasets. Please raise a Github issue if you need assistance of have any questions on the research. 
<p></p>

**Huawei Noah's Ark Lab**

### [[Paper]](https://arxiv.org/pdf/1911.13175)  [[Supplementary]](https://sjmoran.github.io/pdfs/CURL_supplementary.pdf) [[Video]](https://youtu.be/66FnRfDR_Oo) [[Poster]](https://sjmoran.github.io/pdfs/CURL_ICPR_POSTER.pdf) [[Slides]](https://sjmoran.github.io/pdfs/DeepLPFDataBites.pdf) 

<p align="center">
<img src="./images/teaser.PNG" width="80%"/>
</p>

<p align="center">
<a href="https://www.youtube.com/watch?v=Sxach3FM6FY" span>
   <img src="./images/youtube-thumbnail.png" width="90%"/>
</a>
<a href="https://github.com/sjmoran/sjmoran.github.io/blob/490a37c14e5f59db4e1df5034d8cc57444468d1c/pdfs/DeepLPF_CVPR20_poster.pdf" span>
   <img src="./images/poster-img.png" width="100%"/>
</a>
</p>

### Requirements

_requirements.txt_ contains the Python packages used by the code.

### How to train CURL and use the model for inference

#### Training CURL

Instructions:

To get this code working on your system / problem you will need to edit the data loading functions, as follows:

1. main.py, change the paths for the data directories to point to your data directory
2. data.py, lines 248, 256, change the folder names of the data input and output directories to point to your folder names

To train, run the command:

```
python3 main.py
```

<p align="center">
<img src="./images/curl_training_loss.png" width="80%"/>
</p>

#### Inference - Using Pre-trained Models for Prediction

The directory _pretrained_models_ contains a set of four CURL pre-trained models on the Adobe5K_DPE dataset, each model output from different epochs. The model with the highest validation dataset PSNR (23.46dB) is at epoch 99:

* curl_validpsnr_23.45627680277279_validloss_0.02825431153178215_testpsnr_23.929761817622282_testloss_0.026055289432406425_epoch_99_model.pt

This pre-trained CURL model obtains 23.93dB and 0.908 SSIM on the test dataset for Adobe DPE.

To use this model for inference:

1. Place the images you wish to infer in a directory e.g. ./adobe5k_dpe/curl_example_test_input/. Make sure the directory path has the word "input" somewhere in the path.
2. Place the images you wish to use as groundtruth in a directory e.g. ./adobe5k_dpe/curl_example_test_output/. Make sure the directory path has the word "output" somewhere in the path.
3. Place the names of the images (without extension) in a text file in the directory above the directory containing the images i.e. ./adobe5k_dpe/ e.g. ./adobe5k_dpe/images_inference.txt
4. Run the command and the results will appear in a timestamped directory in the same directory as main.py:

```
python3 main.py --inference_img_dirpath=./adobe5k_dpe/ --checkpoint_filepath=./pretrained_models/curl_validpsnr_23.45627680277279_validloss_0.02825431153178215_testpsnr_23.929761817622282_testloss_0.026055289432406425_epoch_99_model.pt 
```

### CURL for RGB images

- __rgb_ted.py__ contains the TED model for RGB images 

### CURL for RAW images

- __raw_ted.py__ contains the TED model for RGB images 

### Github user contributions

__CURL_for_RGB_images.zip__ is a contribution (RGB model and pre-trained weights) courtsey of Github user [hermosayhl](https://github.com/hermosayhl)

### Bibtex

If you do use ideas from the paper in your research please kindly consider citing as below:

```
@misc{moran2019curl,
    title={CURL: Neural Curve Layers for Global Image Enhancement},
    author={Sean Moran and Steven McDonagh and Gregory Slabaugh},
    year={2019},
    eprint={1911.13175},
    archivePrefix={arXiv},
    primaryClass={eess.IV}
}
```

### Datasets

* __Samsung S7__ (110 images, RAW, RGB pairs): this dataset can be downloaded [here](https://www.kaggle.com/knn165897/s7-isp-dataset). The validation and testing images are listed below, the remaining images serve as our training dataset. For all results in the paper we use random crops of patch size 512x512 pixels during training.

  * __Validation Dataset Images__

    * S7-ISP-Dataset-20161110_125321
    * S7-ISP-Dataset-20161109_131627
    * S7-ISP-Dataset-20161109_225318
    * S7-ISP-Dataset-20161110_124727
    * S7-ISP-Dataset-20161109_130903
    * S7-ISP-Dataset-20161109_222408
    * S7-ISP-Dataset-20161107_234316
    * S7-ISP-Dataset-20161109_132214
    * S7-ISP-Dataset-20161109_161410
    * S7-ISP-Dataset-20161109_140043


  * __Test Dataset Images__
  
    * S7-ISP-Dataset-20161110_130812
    * S7-ISP-Dataset-20161110_120803
    * S7-ISP-Dataset-20161109_224347
    * S7-ISP-Dataset-20161109_155348
    * S7-ISP-Dataset-20161110_122918
    * S7-ISP-Dataset-20161109_183259
    * S7-ISP-Dataset-20161109_184304
    * S7-ISP-Dataset-20161109_131033
    * S7-ISP-Dataset-20161110_130117
    * S7-ISP-Dataset-20161109_134017

* __Adobe-DPE__ (5000 images, RGB, RGB pairs): this dataset can be downloaded [here](https://data.csail.mit.edu/graphics/fivek/). After downloading this dataset you will need to use Lightroom to pre-process the images according to the procedure outlined in the DeepPhotoEnhancer (DPE) [paper](https://github.com/nothinglo/Deep-Photo-Enhancer). Please see the issue [here](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/38#issuecomment-449786636) for instructions. Artist C retouching is used as the groundtruth/target. Note, that the images should be extracted in sRGB space. Feel free to raise a Gitlab issue if you need assistance with this (or indeed the Adobe-UPE dataset below). You can also find the training, validation and testing dataset splits for Adobe-DPE in the following [file](https://www.cmlab.csie.ntu.edu.tw/project/Deep-Photo-Enhancer/%5BExperimental_Code_Data%5D_Deep-Photo-Enhancer.zip). 

* __Adobe-UPE__ (5000 images, RGB, RGB pairs): this dataset can be downloaded [here](https://data.csail.mit.edu/graphics/fivek/). As above, you will need to use Lightroom to pre-process the images according to the procedure outlined in the Underexposed Photo Enhancement Using Deep Illumination Estimation (DeepUPE) [paper](https://github.com/wangruixing/DeepUPE) and detailed in the issue [here](https://github.com/wangruixing/DeepUPE/issues/26). Artist C retouching is used as the groundtruth/target. You can find the test images for the Adobe-UPE dataset at this [link](https://drive.google.com/file/d/1HZnNgptNxjKJAhekz2K5yh0mW0yKIws2/view?usp=sharing).

### License

BSD-3-Clause License

### Contributions

We appreciate all contributions. If you are planning to contribute back bug-fixes, please do so without any further discussion.

If you plan to contribute new features, utility functions or extensions to the core, please first open an issue and discuss the feature with us. Sending a PR without discussion might end up resulting in a rejected PR, because we might be taking the core in a different direction than you might be aware of.
