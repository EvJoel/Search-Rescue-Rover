#!/usr/bin/env python

import serial
import rospy
from std_msgs.msg import String


def gpsPublisher():
    
    rospy.init_node("gpspublisher", anonymous=1)
    gpsData = rospy.Publisher("gpsData",String,queue_size=1)
    
    
    try:
        ser = serial.Serial(
            port='/dev/ttyACM1',
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )
        
    except:
        print "Couldn't open serial port"
        
    
    
    while not rospy.is_shutdown():
        
        msg = ser.readlines(1)
        
        gpsData.publish(str(msg))
        
if __name__ == '__main__':
    try:
        gpsPublisher()
        
    except:
        pass
