# example of preparing the horses and zebra dataset
from os import listdir
from numpy import asarray
from numpy import vstack
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from numpy import savez_compressed
 
# load all images in a directory into memory
def load_images(path, size=(128,128)):
	data_list = list()
	# enumerate filenames in directory, assume all are images
	for filename in listdir(path):
		# load and resize the image
		pixels = load_img(path + filename, target_size=size)
		# convert to numpy array
		pixels = img_to_array(pixels)
		# store
		data_list.append(pixels)
	return asarray(data_list)
 
path = "augan-summer-winter-master/datasets/bdd100k/" 
 
# load dataset A
# dataA = load_images(path + 'trainA/resized_128/') # added "resized/", changed from dataA1 to dataA
dataA = load_images(path + 'testA/resized/') # added "resized/"
# dataA = vstack((dataA1, dataA2))
print('Loaded dataA: ', dataA.shape)

# load dataset B
#dataB = load_images(path + 'trainB/resized_128/') # added "resized/", changed from dataB1 to dataB
dataB = load_images(path + 'testB/resized/') # added "resized/"
# dataB = vstack((dataB1, dataB2))
print('Loaded dataB: ', dataB.shape)

# save as compressed numpy array
filename = 'summer2winter_128_test.npz'
savez_compressed(filename, dataA, dataB)
print('Saved dataset: ', filename)