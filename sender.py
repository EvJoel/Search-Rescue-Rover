#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time


def sendMessages():
    rospy.init_node("sender",anonymous=True)
    send = rospy.Publisher("arduinoMessagesSend",String,queue_size=1)
    rate = rospy.Rate(100)
    
    while not rospy.is_shutdown():
        send.publish("1,5")
        rate.sleep()
    
    
    
    
    
if __name__ == '__main__':
    try:
        sendMessages()
    except:
        pass
