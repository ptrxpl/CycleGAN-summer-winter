# cyclegan-summer-winter

### Source and dataset
Source: https://machinelearningmastery.com/cyclegan-tutorial-with-keras/ <br>
Dataset: https://github.com/ptrxpl/augan-summer-winter/tree/master/datasets/bdd100k

### Versions
Script packages_version.py

Python version: <br>
3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] <br>
Numpy version: <br>
1.23.2 <br>
Tensorflow version: <br>
2.9.1 <br>
Matplotlib version: <br>
3.5.3 <br>

### General information
CycleGAN with summer-winter dataset, trained on GTX 1050 (laptop). <br>
The training lasted from August 16 (23:00) to August 19 (20:45) 2022 - non-stop. <br>
162480 iterations were performed (summer data was 2031), so 80 epochs were run. <br>
To run scripts, you need to generate .npz files with generate_npz_file.py script (they are not uploaded here because of size - over 100 MB). <br>

### What changed in the script:
- size 128x128 images - before generate .npz file, use "resize_script.py" in repo augan-summer-winter/datasets/bdd100k
- "Next, we can define a function that will create the 9-resnet block version for 256 × 256 input images. This can easily be changed to the 6-resnet block version by setting image_shape to (128x128x3) and n_resnet function argument to 6 . "
- the model is saved every 2 epochs (40 saved models, AtoB and with BtoA)

### Selected model
The model from iteration 105612 (epoch 52) was chosen because it provides the best results according to screenshots. The final epochs showed dA close to or equal to zero - the failure to teach these epochs. <br>
Additionally, quoting (from source website): <br>
> I suspect that better quality results could be achieved with an additional 100 training epochs with weight decay, as is used in the paper, and perhaps with a data generator that systematically works through each dataset rather than randomly sampling.

### cyclegan_adhoc_img_translate.py
After training and picked model (from visual assessment of files in AtoB generated and BtoA generated folders), this script generated images ad hoc:<br>
Summer to winter: <br>
![Summer to winter](https://github.com/ptrxpl/cyclegan-summer-winter/blob/main/adhoc/AtoB/5.png "Summer to winter") <br>
![Summer to winter](https://github.com/ptrxpl/cyclegan-summer-winter/blob/main/adhoc/AtoB/2.png "Summer to winter") <br>
<br>
Winter to summer: <br>
![Winter to summer](https://github.com/ptrxpl/cyclegan-summer-winter/blob/main/adhoc/BtoA/2.png "Winter to summer") <br>
![Winter to summer](https://github.com/ptrxpl/cyclegan-summer-winter/blob/main/adhoc/BtoA/4.png "Winter to summer") <br>
<br>
More in "adhoc" folder.
