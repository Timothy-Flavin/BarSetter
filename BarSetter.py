from __future__ import print_function
#from pyimagesearch.basicmotiondetector import BasicMotionDetector
import imutils
from imutils.video import VideoStream
import numpy as np
import datetime
import time
import cv2
import os
# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
webcam = VideoStream(src=0).start()
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
# initialize the two motion detectors, along with the total
# number of frames read
#camMotion = BasicMotionDetector()
#piMotion = BasicMotionDetector()
#total = 0
#cap = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(1)
stst=True
numVideos=0
numFrames=0

os.mkdir("video0")


def startStop(event,x,y,flags,userdata):
	global stst, numVideos, numFrames
	if(event==cv2.EVENT_LBUTTONDOWN and x>208 and x<272 and y<32 and bool(stst)):
		stst=False
	elif(event==cv2.EVENT_LBUTTONDOWN and x>208 and x<272 and y<32 and not bool(stst)):
		stst=True
		numVideos+=1
		numFrames=0
		os.mkdir("video"+str(numVideos))

cv2.namedWindow("frame",cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback("frame",startStop)
startImg = cv2.imread("Start.png")
stopImg = cv2.imread("Stop.png")

def drawButton(x,y):
	global frame, startImg, stopImg, stst
	img = 0
	if stst:
		img = stopImg
	else:
		img=startImg
	for i in range(img.shape[0]*img.shape[1]):
		frame[y+int(i/img.shape[1]),x+int(i%img.shape[1])]=img[int(i/img.shape[1]),int(i%img.shape[1])]


while(True):
	while stst:
		frame = webcam.read()
		frame = cv2.resize(frame,(240,320))
		#print("read webcam")
		frame2 = picam.read()
		frame2 = cv2.resize(frame2,(240,320))
		#print("read picam")
		frame = np.concatenate((frame,frame2),axis=1)
		#cv2.namedWindow("frame1",cv2.WINDOW_AUTOSIZE)
#cv2.imshow("frame1",frame)
		cv2.imwrite("video"+str(numVideos)+"/frame"+str(numFrames)+".jpg",frame)
		drawButton(208,0)
		cv2.imshow("frame",frame)
		cv2.waitKey(5)
		numFrames+=1
#cv2.waitKey(1)
	print("not in the whie")
#	cv2.imshow(np.zeros((320,480,3),np.uint8))
	drawButton(208,0)
	cv2.imshow("frame",frame)
	cv2.waitKey(5)

