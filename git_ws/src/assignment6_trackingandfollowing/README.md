# Assignment 6
This assignment consisted of two parts. For part 1, we implemented a line following algorithm on the Turtlebot 3 Burger, both in Gazebo and in the real world. Part 2 used April tags and had the robot identify and follow different April tags around the room. The Python implementation of these can be found in the [scripts](/git_ws/src/assignment6_trackingandfollowing/src/scripts) folder. Videos of the implementations being run on the turtlebot and screen recordings are shown in [videos](/git_ws/src/assignment6_trackingandfollowing/src/videos). 


# Part 1 Turtlebot3 Line Tracking
## (a) Line Tracking in Gazebo 
[Full Video Link](/git_ws/src/assignment6_trackingandfollowing/src/videos/linefollowing_gazebo.mp4)

![Gazebo Line Following](https://github.com/ameyarsalvi/AuE893_Group1_sp21/blob/main/git_ws/src/assignment6_trackingandfollowing/src/videos/linefollowing_gazebo.gif)

After starting roscore, run the launch file to run the gazebo line tracking simulation

Command: `roslaunch assignment6_trackingandfollowing turtlebot3_follow_line.launch`

This launch file opens the Gazebo world and runs the python script `follow_line_step_hsv.py`.  

The procedure implemented in this script is as follows:
1. Subscribe to the topic `"/camera/rgb/image_raw"` to obtain camera data. 
2. Crop the image to only view the region directly in front of the bot. 
3. Threshold the image according to the color of the track to be detected.  This is the yellow color in the gazebo simulation.
4. Calculate the centroid of the blob of the image representing the track.
5. Implement a proportional controller to adjust the angular velocity command to steer this centroid to the center of the image frame.

## (b) Real world Line Tracking
[Full Video Link](/git_ws/src/assignment6_trackingandfollowing/src/videos/TurtleBot_LineFollowing_Real.mp4)

![Turtlebot Line Tracking](https://github.com/ameyarsalvi/AuE893_Group1_sp21/blob/main/git_ws/src/assignment6_trackingandfollowing/src/videos/TurtleBot_LineFollowing_Real.gif)

<img src="https://github.com/ameyarsalvi/AuE893_Group1_sp21/blob/main/git_ws/src/assignment6_trackingandfollowing/src/videos/linefollowing_bot_mask_crop.gif" width="500">

After starting roscore you'll need to ssh into the raspberrypi. Once you are ssh'd in, run the following commands to start the camera and robot:

`pi@raspberrypi$ roslaunch turtlebot3_bringup turtlebot3_robot.launch`

`pi@raspberrypi$ roslaunch raspicam_node camerav2_1280x720.launch enable_raw:=true`

Once this is complete, you can simply execute the python script from the command line on the remote PC. 

`python3 follow_line_step_hsv_BOT.py`

This script executes the same image processing and controller from part 1, but with controller gains and speeds chosen to better accomodate the physical TurtleBot.
# Part 2: April Tags
[April Tag Following Video](/git_ws/src/assignment6_trackingandfollowing/src/videos/AprilTagFollowing_final.mp4)
/
[April Tag Following Screen Video](/git_ws/src/assignment6_trackingandfollowing/src/videos/AprilTag_Screen.mp4)

![April Tag Following](https://github.com/ameyarsalvi/AuE893_Group1_sp21/blob/main/git_ws/src/assignment6_trackingandfollowing/src/videos/AprilTagFollowing.gif)
![April Tag Following Screen](https://github.com/ameyarsalvi/AuE893_Group1_sp21/blob/main/git_ws/src/assignment6_trackingandfollowing/src/videos/AprilTag_Screen.gif)

In order to use the apriltags in ROS you'll need to clone the two git repositories into your src folder:

https://github.com/AprilRobotics/apriltag_ros

https://github.com/AprilRobotics/apriltag

Once these have been cloned you'll need to go back to the catkin workspace (git_ws) and call catkin_make. Once the make has run and compiled, source the setup.bash found in the devel folder. 

To execute the April Tag tracking on the bot, you need to do the same bringup from Part 1 via an ssh connection.  

Once the TurtleBot and camera have been brought up, you canexecute the python script from the command line on the remote PC. 

`python3 tagdemo3.py`

This script uses the 'apriltag' package to detect the apriltag and extract the coordinates of its center.  Then it implements the same proportional controller from part 1 to steer the bot towards the April Tag.  If no tag is detected, a velocity of zero is commanded to the bot.  
