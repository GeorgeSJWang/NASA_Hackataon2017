
# MLP for Pima Indians Dataset Serialize to JSON and HDF5
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

from scipy import misc
from keras import backend as K
import numpy as np

import os

# load json and create model
json_file = open('model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model1.h5")
print("Loaded model from disk")

test_x = np.array([None] * 6)
for i in range(6):
	fin = 'cut' + str(i) + '.png'
	arr = np.sum(misc.imread(fin), axis=2)
	arr = arr.reshape(1, 28, 28, 1)
	# prin
	# t model.predict_classes([arr])
	# test_y = np.array([None] * 10).reshape(1, 10)
	loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
	test_y = loaded_model.predict(arr)
	# score = loaded_model.evaluate(arr, test_y, verbose=0)
	print test_y
	# print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

	# print arr


# 	test_x[i] = arr
# 	print "XD"
# 	# test_x = np.concatenate((test_x, arr), axis)
# print type(test_x)
