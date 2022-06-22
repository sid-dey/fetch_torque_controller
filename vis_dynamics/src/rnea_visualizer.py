#!/root/.local/share/virtualenvs/kinova_control-WdZgPU9p/bin/python
import rospy
import matplotlib.pyplot as plt
import message_filters
from roahm_msgs.msg import debug

# class Plotter:

#     fig, axs = plt.subplots(7, 1)

#     @staticmethod
#     def plot_callback(pos, des):
#         global counter
#         if counter % 10 == 0:
#             stamp = pos.header.stamp
#             time = stamp.secs + stamp.nsecs * 1e-9
#             for i in range(7):
#                 axs[i, 0].plot(time, pos.pos[i], 'b*')
#                 axs[i, 0].plot(time, des.pos_d[i], 'r*')
#                 axs[i, 0].axis("equal")
#                 axs[i, 0].draw()
#                 axs[i, 0].pause(0.00000000001)

#         counter += 1

# if __name__ == '__main__':
#     counter = 0

#     rospy.init_node("rnea_visualizer")

#     pos = message_filters.Subscriber('/joint_info', joints)
#     des = message_filters.Subscriber('/desired', desired)

#     ts = message_filters.TimeSynchronizer([pos, des], 10)
#     ts.registerCallback(Plotter.plot_callback)

#     plt.ion()
#     plt.show()
#     rospy.spin()


class Plotter:

    fig, axs = plt.subplots(7, 1)

    @staticmethod
    def plot_debug(pos):
        stamp = pos.header.stamp
        time = stamp.secs + stamp.nsecs * 1e-9
        for i in range(7):
            Plotter.axs[i].plot(time, pos.pos[i], 'b*')
            Plotter.axs[i].plot(time, pos.pos_d[i], 'r*')
            Plotter.axs[i].axis("equal")
            # plt.draw()
            # plt.pause(0.00000000001)


if __name__ == '__main__':
    counter = 0

    rospy.init_node("rnea_visualizer")

    pos_sub = rospy.Subscriber('/debug', debug, Plotter.plot_debug)

    # pos = message_filters.Subscriber('/joint_info', joints)
    # des = message_filters.Subscriber('/desired', desired)

    # ts = message_filters.TimeSynchronizer([pos, des], 10)
    # ts.registerCallback(Plotter.plot_callback)

    plt.ion()
    plt.show(block=True)
    # rospy.spin()
