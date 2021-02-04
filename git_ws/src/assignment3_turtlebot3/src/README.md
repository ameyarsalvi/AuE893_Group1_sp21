Here is a readme for assignment 3

## Running the circle program
The python scripts for assignment 2 were modified to control the turtlebot in Gazebo. The turtlebot 3 burger moves in a circular path. The launch file creates a empty world in Gazebo and lauches the program circle.py. Finaly, the circle.py script is ran through Gazebo which makes the turtlebot move in a circle.

Command: roslaunch assignment3_turtlebot3 move.launch code:=circle


## Running the square program
The python scripts for assignment 2 were modified to control the turtlebot in Gazebo. the turtlebot  3 burger moves in a square path. The launch file creates an empty world in Gazebo and launches the program square.py. Finally, the square.py script is ran throgh Gazebo which makes the turtlebot move in a square

Command: roslaunch assignment3_turtlebot3 move.launch code:=square

## Running the Emergency brake program
The emergency brake program requires 1) turtlebot3_empty_world.launch file to launch the program, 2) emergency_braking.py Python script which contains the braking code and 3) emptywwall.world file which contains the empty world with a wall in front of turtlebot

Command : roslaunch assignment3_turtlebot3 turtlebot3_empty_world.launch
