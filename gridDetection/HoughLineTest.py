import  cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

while True:
	#Capture frame-by-frame
	ret, frame = cap.read()

	#Operations on the frame go here
	frame = imutils.resize(frame, width = 500)
	grayCap = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(grayCap,50,150,apertureSize = 3)

	lines = cv2.HoughLines(edges,2,np.pi/180,200)
	
	if lines is not None:
		for line in lines:
			for rho,theta in line:
				a = np.cos(theta)
				b = np.sin(theta)
				x0 = a*rho
				y0 = b*rho
				x1 = int(x0 + 1000*(-b))
				y1 = int(y0 + 1000*(a))
				x2 = int(x0 - 1000*(-b))
				y2 = int(y0 - 1000*(a))

				cv2.line(frame, (x1,y1), (x2,y2), (0,0,255),2)


	cv2.imshow('frame', frame)
	cv2.imshow('edges', edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

camera.release()
cv2.destroyAllWindows()
