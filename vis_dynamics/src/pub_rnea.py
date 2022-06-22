#!/usr/bin/env python3
import rospy
from roahm_msgs.msg import debug
import numpy as np


def talker():
    pub_debug = rospy.Publisher('/debug', debug, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    count = 0
    while not rospy.is_shutdown():
        count += 1
        curr = debug()
        curr.header.stamp = rospy.get_rostime()
        curr.header.frame_id = str(count)

        curr.pos = np.array([count - 10 * i for i in range(7)])
        curr.vel = np.array([count - 10 * i for i in range(7)])
        curr.acc = np.array([count - 10 * i for i in range(7)])

        curr.pos_d = np.array([2 * count - 10 * i for i in range(7)])
        curr.vel_d = np.array([2 * count - 10 * i for i in range(7)])
        curr.acc_d = np.array([2 * count - 10 * i for i in range(7)])

        curr.torque = np.array([2 * count - 10 * i for i in range(7)])
        curr.torque_d = np.array([count - 10 * i for i in range(7)])

        curr.e = np.array([2 * count - 10 * i for i in range(7)])
        curr.ed = np.array([count - 10 * i for i in range(7)])

        rospy.loginfo(curr.header.frame_id)
        pub_debug.publish(curr)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
