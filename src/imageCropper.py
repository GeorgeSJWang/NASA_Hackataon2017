import numpy as np
from scipy import misc
from PIL import Image

test_image = "../Data/captcha_training/image.php-16.png"
original = Image.open(test_image)
original.show()

width, height = original.size   # Get dimensions
left = 0
top = 0
right = width
bottom = 3 * height/5
cropped_example = original.crop((left, top, right, bottom))

cropped_example.show()
cropped_example.save('../Data/captcha_training/image.png')

arr = misc.imread('../Data/captcha_training/image.png')
# print arr
# print arr.shape
a = np.sum(arr, axis =2)
# print a
# print a.shape
b = np.sum(a, axis= 0)
# print b
# print b.shape
head = 0
tail = 0
cnt = 0
# print arr.shape
# print type(arr)
for idx in range(len(b)):
	if b[idx] > 10000:
		if head != tail:
			# for i in arr.shape[0]:
			# 	for j in arr.shape[1]:
			# 		for k in arr.shape[2]:
			tmp = arr[:, tail:head, :]
			print tmp.shape
			
			if tmp.shape[1] < 6:
				blank = np.zeros([16, 10, 3])
				blank.fill(255)
				# for a in range(blank.shape[])
				tmp = np.concatenate((blank, tmp), axis=1)
				tmp = np.concatenate((tmp, blank), axis=1)
			tmp = misc.imresize(tmp, [28, 28, 3])
			
			misc.imsave('cut' + str(cnt) + '.png', tmp)
			# print head, tail
			cnt += 1
		head = idx
		tail = idx
	else:
		tmp = np.sum(arr, axis=2)
		# print '-----------'
		for i in range(arr.shape[0]):
			# print tmp[i, idx]
			if tmp[i, idx] < 700:
				arr[i, idx, 0] = 0
				arr[i, idx, 1] = 0
				arr[i, idx, 2] = 0
			else:
				arr[i, idx, 0] = 255
				arr[i, idx, 1] = 255
				arr[i, idx, 2] = 255
		head = idx


# print len(list(cropped_example.getdata()))