#!/usr/bin/env python3
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist #
import numpy as np

def callback(dt):
    left = min(min(dt.ranges[50:100]),15)
    right = min(min(dt.ranges[260:310]),15)
    #front = min(min(dt.ranges[330:360] + dt.ranges[0:30]),10)
    frontrng = dt.ranges[330:360] + dt.ranges[0:30]
    frontrng = np.array(frontrng)
    frontrng = frontrng[frontrng > 0.0]
    front = min(min(frontrng),10)
    print('-------------------------------------------')
    print('Range data at Front:   {}'.format(front))
    print('Range data at Left:  {}'.format(left))
    print('Range data at Right: {}'.format(right))
    print('-------------------------------------------')
    thr1 = 0.5 # Laser scan range threshold
    thr2 = 0.5
    if front>thr1: # Checks if there are obstacles in front and
                                                                         # 15 degrees left and right (Try changing the
									 # the angle values as well as the thresholds)
        move.linear.x = 0.5 # go forward (linear velocity)
        move.angular.z = 0.0 # do not rotate (angular velocity)
    else:
        move.linear.x = 0.0 # stop
        move.angular.z = 0.7 # rotate counter-clockwise
        if dt.ranges[0]>thr1 and dt.ranges[30]>thr2 and dt.ranges[330]>thr2:
            move.linear.x = 0.4
            move.angular.z = 0.0
    pub.publish(move) # publish the move object


move = Twist() # Creates a Twist message type object
rospy.init_node('obstacle_avoidance_node') # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  # Publisher object which will publish "Twist" type messages
                            				 # on the "/cmd_vel" Topic, "queue_size" is the size of the
                                                         # outgoing message queue used for asynchronous publishing

sub = rospy.Subscriber("/scan", LaserScan, callback)  # Subscriber object which will listen "LaserScan" type messages
                                                      # from the "/scan" Topic and call the "callback" function
						      # each time it reads something from the Topic

rospy.spin() # Loops infinitely until someone stops the program execution
