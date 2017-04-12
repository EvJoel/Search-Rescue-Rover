#!/usr/bin/env python


import time 
import rospy 
import serial
from std_msgs.msg import String

def callback(data):
    arduino_receive = rospy.Publisher("arduinoReceive",String,queue_size=1)
    
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
            if message[0] != "":
                arduino_receive.publish(message)
                print message
            
            ser.write(str(data))
            
            
            print data
        
            ser.flush()
            ser.close()
        except:
            print "couldn't send string"
            pass
    
    
        
        
def sendData():
    rospy.init_node("send",anonymous=True)   
    arduino_messages = rospy.Subscriber("arduinoMessagesSend",String,callback)  
    
    rospy.spin()
    
        
if __name__ == '__main__':
    sendData()
    
    
