# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	
	# Convert to grayscale
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	# Look for faces in the image using the loaded cascade file
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

	# Show the frame
	cv2.imshow("Frame", image)

	# Wait for key
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	
	faceDetected = False
	# Draw a rectangle around every found face
	for (x,y,w,h) in faces:
		faceDetected = True
		# Create rectangle around the face
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
		# Save the image
		cv2.imwrite("result.jpg", image)
