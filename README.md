# cyclegan-summer-winter

### Source and dataset
Source: https://machinelearningmastery.com/cyclegan-tutorial-with-keras/ <br>
Dataset: https://github.com/ptrxpl/augan-summer-winter/tree/master/datasets/bdd100k

### General information
CycleGAN has been tested for dataset summer-winter, on GTX 1050 (laptop). <br>
The training lasted from August 16 (23:00) to August 19 (20:45) - non-stop. <br>
162480 iterations were performed (summer data was 2031), so 80 epochs were run. <br>

### What changed in the script:
- size 128x128 images
- "Next, we can define a function that will create the 9-resnet block version for 256 × 256 input images. This can easily be changed to the 6-resnet block version by setting image_shape to (128x128x3) and n_resnet function argument to 6 . "
- the model is saved every 2 epochs (40 saved models, AtoB and with BtoA)
