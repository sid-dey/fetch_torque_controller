# Debug Information for Visualization
std_msgs/Header header
# HLP Trajectory Provides Desired Values
float32[7] pos_d
float32[7] vel_d
float32[7] torque_d
# Joint Feedback from robot provides Curr Values
float32[7] pos_curr
float32[7] vel_curr
float32[7] torque_curr
# Dynamics Algorithm computes required torque
float32[7] torque_calc
# Dynamics Algorithm computes e, e_d while computing required torque
float32[7] e
float32[7] e_d
