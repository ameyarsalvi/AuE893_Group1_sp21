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
    'front': 0,
    'left': 0,
}
ep = 0
e0 = 0

def clbk_laser(msg):
    global regions_

    regions_ = {
        'right':  min(min(msg.ranges[270:315]),10),
        'front' : min(min(msg.ranges[350:360] + msg.ranges[0:10]),10),
        'left':   min(min(msg.ranges[50:100]),10),
    }
    #while(1):
    #    take_action()


def take_action():
    global regions_,e0,ep
    regions = regions_
    msg = Twist()
    linear_x = 0
    angular_z = 0

    d = 0.5
    df = 0.5
    
    fast = 0.6
    slow = 0.5
    back = -0.2

    #1.2,5
    kp = 1.5
    kd = 5
    e0 = regions['left'] - regions['right']
    
    if regions['front'] > df:
        angular_z = kp*e0 + kd*(e0 - ep)
        if regions['left'] > 2 or regions['right'] > 2:
            linear_x = slow
        else:
            linear_x = fast
    else:
        angular_z = 0.6
        linear_x = 0  
    
    thresh = 1.5
    if angular_z > thresh:
        angular_z = thresh
    elif angular_z < -thresh:
        angular_z = -thresh
    print("Errors:")
    print([e0,e0-ep])
    print("Controls")
    print([angular_z,linear_x])
    ep = e0
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub_.publish(msg)



def main():
    global pub_
    
    rospy.init_node('reading_laser')
    
    pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
    
    rate = rospy.Rate(5)
    while(1):
        msg = Twist()
        take_action()
        #pub_.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass
