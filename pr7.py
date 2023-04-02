import cv2
import numpy as np 
import matplotlib as plt

Webcamstreaming=cv2.VideoCapture(0)

#width= Webcamstreaming.get(cv2.Webcamstreaming_PROP_FRAME_WIDTH)
#height=Webcamstreaming.get(cv2.Webcamstreaming_PROP_FRAME_HEIGHT)

while True: 
	ret, frame = Webcamstreaming.read()
	if ret:
		a=cv2.flip(frame,1)
		b=frame= 255 - frame
		c=gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		d=frame[:,:,2]=255
		frame=np.concatenate([a,b] , [c,d], 2)


		cv2.imshow("Mywebcam", frame)
		q = cv2.waitKey(1)

		if q == ord("q"):
			break


cv2.destroyAllWindows()		
cap.release()