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

### What changed in the script:
- size 128x128 images
- "Next, we can define a function that will create the 9-resnet block version for 256 × 256 input images. This can easily be changed to the 6-resnet block version by setting image_shape to (128x128x3) and n_resnet function argument to 6 . "
- the model is saved every 2 epochs (40 saved models, AtoB and with BtoA)
