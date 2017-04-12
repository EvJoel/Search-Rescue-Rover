#!/usr/bin/env python

import serial
import rospy
import time
from sensor_msgs.msg import Image
from std_msgs.msg import String

def getData():

    arduino_messages = rospy.Publisher("arduino_messages",String, queue_size=1)
    rospy.init_node("getData",anonymous=True)
    while True:
        
        try:
            ser = serial.Serial(
                port='/dev/ttyACM0',
                baudrate=9600,
                parity=serial.PARITY_ODD,
                stopbits=serial.STOPBITS_TWO,
                bytesize=serial.SEVENBITS
            )
            while ser.is_open:
                try:
                    message = ser.readlines(1)
                    temp = message[0].split("%")
                    
                    if temp[0] == 1:
                        arduino_messages.publish(str(message))
                        rospy.loginfo(message)
                    
                    
                    ser.flush()
                    ser.close()
                    
                except:
                    rospy.loginfo("Couldn't read data")    
        except:
            rospy.loginfo("couldn't open port")
        rospy.sleep(1)
        
        
        
def parseData(message):
    pass
        





if __name__ == '__main__':
    try:
        getData()
    except rospy.ROSInterruptException:
        pass
