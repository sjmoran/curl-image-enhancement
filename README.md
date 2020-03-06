# CURL: Neural Curve Layers for Global Image Enhancement (Pre-print, paper under review)

[Sean Moran](http://www.seanjmoran.com),  Ales Leonardis, [Greg Slabaugh](http://gregslabaugh.net/),Steven McDonagh

Huawei Noah's Ark Lab

### [[Paper]](https://arxiv.org/pdf/1911.13175)  [[Supplementary]](http://www.seanjmoran.com/pdfs/CURL_arxiv_supplementary.pdf) 

<p align="center">
<img src="./images/teaser.PNG" width="80%"/>
</p>
Repository for the paper CURL: Neural Curve Layers for Global Image Enhancement. Here you will find the code, pre-trained models, information of the datasets, and information on the training procedure for our models. Please raise a Github issue if you need assistance of have any questions on the research. 
<p></p>

### Bibtex

If you do use ideas from the paper in your research please kindly consider citing as below:

```
@misc{moran2019difar,
    title={CURL: Neural Curve Layers for Global Image Enhancement},
    author={Sean Moran, Ales Leonardis, Gregory Slabaugh, Steven McDonagh}
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
    
* __Adobe-DPE__ (5000 images, RGB, RGB pairs): this dataset can be downloaded [here](https://data.csail.mit.edu/graphics/fivek/). After downloading this dataset you will need to use Lightroom to pre-process the images according to the procedure outlined in the DeepPhotoEnhancer (DPE) [paper](https://github.com/nothinglo/Deep-Photo-Enhancer). Please see the issue [here](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/38#issuecomment-449786636) for instructions. Artist C retouching is used as the groundtruth/target. Feel free to raise a Gitlab issue if you need assistance with this (or indeed the Adobe-UPE dataset below). You can also find the training, validation and testing dataset splits for Adobe-DPE in the following [file](https://www.cmlab.csie.ntu.edu.tw/project/Deep-Photo-Enhancer/%5BExperimental_Code_Data%5D_Deep-Photo-Enhancer.zip). 

* __Adobe-UPE__ (5000 images, RGB, RGB pairs): this dataset can be downloaded [here](https://data.csail.mit.edu/graphics/fivek/). As above, you will need to use Lightroom to pre-process the images according to the procedure outlined in the Underexposed Photo Enhancement Using Deep Illumination Estimation (DeepUPE) [paper](https://github.com/wangruixing/DeepUPE) and detailed in the issue [here](https://github.com/wangruixing/DeepUPE/issues/26). Artist C retouching is used as the groundtruth/target. You can find the test images for the Adobe-UPE dataset at this [link](https://drive.google.com/file/d/1HZnNgptNxjKJAhekz2K5yh0mW0yKIws2/view?usp=sharing).
