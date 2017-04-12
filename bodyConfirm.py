#!/usr/bin/env python

import rospy
import ast
import statistics as stat
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

detectedFaces = [[],[],[],[],[],[],[],[],[],[]]
pub_faces = []

def callback(faces):
    
    
    found_faces = rospy.Publisher("foundFaces",String,queue_size=1)
    faces = str(faces)
    print faces
    rate = rospy.Rate(50)
    #print faces
    #print type(faces)
    
    if(faces != "data: ()"):
        
        print "found face"
        faces = faces[6:]
        faces.replace("data: ","")
        faces = faces.replace(" ", ",")
        faces = faces.replace(",,",",")
        faces = faces.replace("[,","[")
        faces = faces.replace(",,",",")
        
        faces = ast.literal_eval(faces)        
        i = 0
        for face in faces:
                
            detectedFaces[i].append(face)
            #print detectedFaces
            #print detectedFaces[0]
            print len(detectedFaces[0])
            i += 1
        i = 0
        if len(detectedFaces[0]) == 50:
            pub_faces = []
            for i in xrange(len(detectedFaces)):
                face_coords = [[],[],[],[]]
                if len(detectedFaces[i]) > 1:
                    for j in xrange(len(detectedFaces[i])):
                        face_coords[0].append(detectedFaces[i][j][0])
                        face_coords[1].append(detectedFaces[i][j][1])
                        face_coords[2].append(detectedFaces[i][j][2])
                        face_coords[3].append(detectedFaces[i][j][3])
                    pub_faces.append([i,stat.stdev(face_coords[0]),stat.stdev(face_coords[1]),stat.stdev(face_coords[2]),stat.stdev(face_coords[3])])
                    face_coords = []
            
            found_faces.publish(str(pub_faces))
            for i in xrange(len(detectedFaces)):
                detectedFaces[i][:] = []            
            
            print len(detectedFaces[0])
            pub_faces = []
            #print len(pub_faces)
            
    else:
        print "No faces found"
            
            
def confirmBody():
    rospy.init_node("confirmBody",anonymous=1)
    bodyConfirm = rospy.Subscriber("faces", String, callback)
    
    rospy.spin()
    
if __name__ == "__main__":
    confirmBody()
  