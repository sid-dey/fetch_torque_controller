#!/usr/bin/env python
import copy
import actionlib
import rospy
import numpy as np
#import pcl

from math import sin, cos

from geometry_msgs.msg import TwistStamped, PoseStamped
from std_msgs.msg import Int8, Float32
from sensor_msgs.msg import JointState
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from control_msgs.msg import GripperCommandAction, GripperCommandGoal, GripperCommand
# from moveit_msgs.msg import PlaceLocation, MoveItErrorCodes
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

# import moveit_commander

GRIP_TOPIC = "/fetch/grip_state"

NO_DOF = 2

class GripperClient(object):

    def __init__(self, name, joint_names):
        self.grip_state = GripperCommand()
        self.sub_grip_states = rospy.Subscriber(GRIP_TOPIC, GripperCommand, self.handle_grip_states, tcp_nodelay=True,
                                           queue_size=1)
        self.client = actionlib.SimpleActionClient("%s/gripper_action" % name,
                                                   GripperCommandAction)
        
        rospy.loginfo("Waiting for %s..." % name)
        self.client.wait_for_server()
        # self.joint_names = joint_names

        self.grip_state = GripperCommand()
        # self.grip_state.joint_names = joint_names

        self.grip_state.position = 0
        self.grip_state.max_effort = 20

        self.move_to()

        # set up flag for new trajectory received
        self.new_grip_command_received_flag = False

    def handle_grip_states(self, data):
        self.grip_state.position = data.position
        self.grip_state.max_effort = data.max_effort
        self.new_grip_command_received_flag = True

    def move_to(self):
        gripper_goal = GripperCommandGoal()
        gripper_goal.command = self.grip_state
        self.new_grip_command_received_flag = False
        
        self.client.send_goal(gripper_goal)
        # self.client.wait_for_result()

if __name__ == "__main__":
    # Create a node
    rospy.init_node("fetch_grasping_interface")

    # Make sure sim time is working
    while not rospy.Time.now():
        pass

    # Setup clients
    gripper_action = GripperClient("gripper_controller", ["l_gripper_finger_joint", "r_gripper_finger_joint"])
    rospy.loginfo("Moving the gripper with gripper commands")

    while not rospy.is_shutdown():
        if gripper_action.new_grip_command_received_flag:
            gripper_action.move_to()

