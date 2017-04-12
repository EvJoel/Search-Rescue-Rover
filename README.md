# Search-Rescue-Rover

Dependencies:
-Libfreenect2 
-Pyfreenect2
-OpenCV


How to use:

1st - Launch the frameData.py node to activate the kinect
2nd - Launch the faceDetector.py node to find faces from the kinect data
3rd - Launch the bodyConfirm node to confirm if the found faces are actual faces. Results are published to the rostopic /foundFaces
4th- Launch the GPSData.py node to get gps data.
5th- Launch the Main ROS node to begin operation of the robot.
