import cv2
import numpy as np 
CHAR_LIST = '$@B%8&WM#*oahkndpqwmZOOQLCJUYXzcuvunxrjit/\|()1{}[]?-_+~<>i!LI;:,\"^`'.  23
image = cv2.imread('anhchuydoi.jpg', 0)
num_cols = 20
height, width = image.shape
cell_width = width / 20
cell_height = cell_width * 2
num_rows = int(height / cell_height)
#print(cell_width)
#print(image)
cv2.imshow('IMAGE', image[0:300, :])
cv2.waitKey(0)
for i in range(num_rows):
	for j in range(num_cols):
		sub_image = image[int(i*cell_height): int((i+1)*cell_height), int(j*cell_width): int((j+1)*cell_width)]
		index = int(np.mean(sub_image)/255*len(CHAR_LIST))
		print(index)