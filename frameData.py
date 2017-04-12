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
log.basicConfig(filename='webcam.log',level=log.INFO)

#cv2.namedWindow("RGB")
anterior = 0

# Initialize device
serialNumber = pyfreenect2.getDefaultDeviceSerialNumber()
kinect = pyfreenect2.Freenect2Device(serialNumber)

# Set up signal handler
shutdown = False
def sigint_handler(signum, frame):
    print "Got SIGINT, shutting down..."
    shutdown = True
signal.signal(signal.SIGINT, sigint_handler)


def frameData():
    
    
    rgb_frames = rospy.Publisher("rgbFrames",Image,queue_size=1)
    depth_frames = rospy.Publisher("depthFrames",Image,queue_size=1)
    #ir_frame = rospy.Publisher("irFrames",Image,queue_size=1)
    
    rospy.init_node("frameData",anonymous=True)
    
    rate = rospy.Rate(100)
    
    while not rospy.is_shutdown():
       
        # Set up frame listener
        frameListener = pyfreenect2.SyncMultiFrameListener(pyfreenect2.Frame.COLOR,pyfreenect2.Frame.IR,pyfreenect2.Frame.DEPTH)
    
        
        kinect.setColorFrameListener(frameListener)
        kinect.setIrAndDepthFrameListener(frameListener)
    
        # Start recording
        kinect.start()
    
        # Print useful info
        print "Kinect serial: %s" % kinect.serial_number
        print "Kinect firmware: %s" % kinect.firmware_version
    
        # What's a registration?
        print kinect.ir_camera_params
    
        registration = pyfreenect2.Registration(kinect.ir_camera_params, kinect.color_camera_params)
        #registration = pyfreenect2.Registration(kinect.color_camera_pacdrams, kinect.ir_camera_params)
        #registration = pyfreenect2.Registration()
    
       
        frames = frameListener.waitForNewFrame()
       
        rgbFrame = frames.getFrame(pyfreenect2.Frame.COLOR)
        #irFrame = frames.getFrame(pyfreenect2.Frame.IR)
        depthFrame = frames.getFrame(pyfreenect2.Frame.DEPTH) 
        
        bridge = CvBridge()
        
        rgb_frame = rgbFrame.getRGBData()
        depth_frame = depthFrame.getDepthData()
        
        rgbFramesROS = bridge.cv2_to_imgmsg(rgb_frame, encoding="passthrough")
        depthFramesROS = bridge.cv2_to_imgmsg(depth_frame, encoding="passthrough")
        
        rgb_frames.publish(rgbFramesROS)
        depth_frames.publish(depthFramesROS)
        
        rate.sleep()

    
if __name__ == '__main__':
    try:
        frameData()
    except rospy.ROSInterruptException:
        pass



                    
