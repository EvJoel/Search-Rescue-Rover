#!/usr/bin/env python

import cv2
import scipy.misc
import signal
import pyfreenect2
import sys 
import datetime as dt
import logging as log
import time 
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cascPath = "/home/prometheus/catkin_ws/src/serial_test/scripts/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

anterior = 0

#cv2.namedWindow("RGB")

def callback(data):
    #print "hello"
    face_pub = rospy.Publisher("faces",String,queue_size=1)
    bridge = CvBridge()
    
    rgb_frameROS = data
    
    rgb_frame = bridge.imgmsg_to_cv2(rgb_frameROS,"passthrough")
    
    
    
    bgr_frame = rgb_frame.copy()
    bgr_frame[:,:,0] = rgb_frame[:,:,2]
    bgr_frame[:,:,2] = rgb_frame[:,:,0]
    
    bgr_frame_resize = scipy.misc.imresize(bgr_frame, size = .5)
    gray = cv2.cvtColor(bgr_frame_resize, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        )
    print type(faces)
    print "face found at " + str(faces)
    
    face_pub.publish(str(faces))
    #for (x, y, w, h) in faces:
        #cv2.rectangle(bgr_frame_resize, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #print "Found Face .. ."    
    
    #cv2.imshow("RGB", bgr_frame_resize)
    
    
    #face_pub.publish(faces)
    
    

def faceDetector():
    
    rospy.init_node('faceDetector',anonymous=True)
    rospy.Subscriber("rgbFrames", Image, callback)
   
    
    rospy.spin()
    
if __name__ == '__main__':
    faceDetector()
    

      
    
    
