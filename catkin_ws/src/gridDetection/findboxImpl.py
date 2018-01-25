import findbox as fb
import os
import cv2

dir = raw_input('Enter a directory to look for images: ')
fileList = os.listdir(dir)

for file in fileList:
	cv2.imshow(file, fb.detect_box(os.path.join(dir, file)))
	cv2.waitKey(0)

