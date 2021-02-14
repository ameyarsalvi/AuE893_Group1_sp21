#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf import transformations
import math

pub_ = None
regions_ = {
    'right': 0,
    'fright': 0,
    'front': 0,
    'fleft': 0,
    'left': 0,
}

def clbk_laser(msg):
    global regions_

    frontl = msg.ranges[0:45]
    frontr = msg.ranges[315:359]
    frontt = frontl + frontr

    regions_ = {
        'right':  min(min(msg.ranges[270:314]), 10),
        'front' : min(min(frontt), 10),
        'left':   min(min(msg.ranges[46:90]), 10),
    }
    #while(1):
    #    take_action()

def take_action():
    global regions_
    regions = regions_
    msg = Twist()
    linear_x = 0
    angular_z = 0

    d = 1
    
    if regions['front'] > d and regions['fleft'] > d and regions['fright'] > d:
        angular_z = 0
        linear_x = 0.5
    elif regions['front'] < d and regions['fleft'] > d and regions['fright'] > d:
        angular_z = -1.5
        linear_x = 0
    elif regions['front'] > d and regions['fleft'] > d and regions['fright'] < d:
        angular_z = -1.5
        linear_x = 0
    elif regions['front'] > d and regions['fleft'] < d and regions['fright'] > d:
        angular_z = 1.5
        linear_x = 0
    elif regions['front'] < d and regions['fleft'] > d and regions['fright'] < d:
        angular_z = -1.5
        linear_x = 0
    elif regions['front'] < d and regions['fleft'] < d and regions['fright'] > d:
        angular_z = 1.5
        linear_x = 0
    elif regions['front'] < d and regions['fleft'] < d and regions['fright'] < d:
        angular_z = 0
        linear_x = -0.5
    else:
        angular_z = 0
        linear_x = 0.5
    
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub_.publish(msg)



def main():
    global pub_
    
    rospy.init_node('reading_laser')
    
    pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
    
    rate = rospy.Rate(20)
    while(1):
        msg = Twist()
        take_action()
        #pub_.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass