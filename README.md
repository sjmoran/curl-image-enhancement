# DIFAR: Deep Image Formation and Retouching

### [[Paper]](https://arxiv.org/pdf/1911.13175) 

<p align="center">
<img src="./images/teaser.png" width="80%"/>
<a href="https://www.youtube.com/watch?v=d7OXb2sqoec" span>
   <img src="./images/youtube-thumbnail.png" width="90%"/>
</a>
<a href="https://www.cmlab.csie.ntu.edu.tw/project/Deep-Photo-Enhancer/CVPR-2018-DPE-poster-compress.pdf" span>
   <img src="./images/poster-img.png" width="100%"/>
</a>
</p>
TensorFlow implementation of the CVPR 2018 spotlight paper, Deep Photo Enhancer: Unpaired Learning for Image Enhancement from Photographs with GANs. If you use any code or data from our work, please cite our paper.

### [Update Jun. 05, 2019] Rename Model script
I add the `rename_model.py` to the download link below.

### [Update Mar. 31, 2019] Inference Models (Supervsied and Unsupervised).
Download link: [here](https://www.cmlab.csie.ntu.edu.tw/project/Deep-Photo-Enhancer/[Online_Demo_Models]_Deep-Photo-Enhancer.zip). The code is exactly the same I used in my demo website. (Sorry, I do not have time to polish it...)
Simplified tutorial: Using the function `getInputPhoto` and `processImg` in the `TF.py`

### [Update Dec. 18, 2018] Data and Code (Supervsied and Unsupervised).
There are too many people asked me to release the code even the code is not polished and is ugly as me. Therefore, I put my ugly code and the data [here](https://www.cmlab.csie.ntu.edu.tw/project/Deep-Photo-Enhancer/[Experimental_Code_Data]_Deep-Photo-Enhancer.zip). I also provide the [supervised code](https://www.cmlab.csie.ntu.edu.tw/project/Deep-Photo-Enhancer/[Experimental_Supervised_Code]_Deep-Photo-Enhancer.zip). There are a lot of unnecessary parts in the code. I will refactor the code ASAP. Regarding the data, I put the name of the images we used on [MIT-Adobe FiveK dataset](https://data.csail.mit.edu/graphics/fivek/). I directly used Lightroom to decode the images to TIF format and used Lightroom to resize the long side of the images to 512 resolution (The label images are from retoucher C). I am not sure whether I have right to release the HDR dataset we collected from [Flickr](https://www.flickr.com/search/?text=HDR) so I put the ID of them. You can download the images according to the IDs. (The code was run on 0.12 version of TensorFlow. The A-WGAN part in the code did not implement decreasing the lambda since the initial lambda was relatively small in that case.)

Some useful issues: [#6](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/6), [#16](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/16), [#18](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/18), [#24](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/24), [#27](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/27), [#38](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/38), [#39](https://github.com/nothinglo/Deep-Photo-Enhancer/issues/39)

### Results

