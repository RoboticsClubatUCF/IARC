#import statements
import numpy as np
import cv2 as cv

def detect_box(image_path):
	#load our image
	img = cv.imread(image_path);

	#backup image
	imgBackup = img;


	#define pure white color
	white = np.array([255,255,255]);


	#mask the image, turn everything else black.
	mask = cv.inRange(img, white, white);

	#find the contours in the image
	(contourImage, contours, _) = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE);
	biggestContour = max(contours, key=cv.contourArea);

	#draw a contour on the old image
	cv.drawContours(img, biggestContour, -1, (0,255,0), 4);

	#output our image
	#cv.imshow("Image", img);
	#cv.waitKey(0);
	#cv.imshow("Image2", thresh);
	#cv.waitKey(0);

	#if we're a function,return the modified image
	return img;
	
