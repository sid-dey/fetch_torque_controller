This repo is meant to test torque control on the Fetch robot arm.

Here, we implement a passivity-based torque controller which is to be run on the Fetch robot hardware (mobile manipulator).
The code has beeen compiled and tested on a Fetch mobile manipulator running Ubuntu 14.04 and ROS Indigo.

From installation to running the controller, the steps are as follows:
1. Create a catkin_ws.
2. Clone this repo into the src directory.
3. Compile this code using catkin_make with the Release build flag.
4. Stop robot `sudo service robot stop`.
5. Source catkin_ws.
6. Restart robot `roslaunch fetch_bringup fetch.launch`.
7. Start torque controller `roslaunch robot_controllers torque_controller.launch`.
8. To send trajectories to the robot arm, publish JointTrajectory msgs to the `/fetch/des_states` rostopic.
9. For logging data, you can consider the `/debug` rostopic, which publishes custom ROS messages of type Roahm::Debug. Check out the roahm_msgs ROS package for more details.

If you have any issues or questions, please reach out to Sid Dey (siddey@umich.edu).