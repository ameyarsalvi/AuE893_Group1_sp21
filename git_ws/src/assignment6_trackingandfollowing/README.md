# Assignment 6
This assignment was split into two parts. For part 1 we were to implement a line following algorithm and test in both Gazebo and the real world. Part 2 used apriltags and had the robot identify and follow different april tags around the room. The implementation of these can be found in the [scripts](/git_ws/src/assignment6_trackingandfollowing/src/scripts) folder. Videos of the implementations being run on the turtlebot and screen recordings are shown in [videos](/git_ws/src/assignment6_trackingandfollowing/src/videos). 


# Part 1: Gazebo Simulation
-->video link<--
After starting roscore, run the launch file to run the gazebo line tracking simulation
Command: `roslaunch assignment6_trackingandfollowing turtlebot3_follow_line.launch`

# Part 1: Turtlebot3 Line Tracking
-->video link<--
After starting roscore you'll need to ssh into the raspberrypi. Once you are ssh'd in, run the following commands to start the camera and robot:
`pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_robot.launch`
`pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch`

Then back on the host computer, you need to run the following command in order to correctly get the subscriber to work:
`rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw`


# Part 2: April Tags
-->video link<--
