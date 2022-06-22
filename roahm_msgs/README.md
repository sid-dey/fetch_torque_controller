# roahm_msgs

This package contain message/service files used in other packages.



## Messages

### joints

Joint information for Kinova Gen3 Arm.

| Name     | Type       | Description            |
| -------- | ---------- | ---------------------- |
| frame_id | uint32     | index of the frame     |
| pos      | float32[7] | position of each joint |
| vel      | float32[7] | velocity of each joint |
| torque   | float32[7] | torque of each joint   |

### dynamics

torque values to be applied on the arm.

| Name     | Type       | Description                        |
| -------- | ---------- | ---------------------------------- |
| frame_id | uint32     | index of the frame                 |
| torques  | float32[7] | torque of each joint to be applied |

### debug

| Name        | Type            | Description                                            |
| ------      | --------------- | ----------------------------------------               |
| header      | std_msgs/Header | header type containing id, timestamps...               |
| pos_d       | float32[7]      | desired position for each joint                        |
| vel_d       | float32[7]      | desired velocity for each joint                        |
| torque_d    | float32[7]      | desired acceleration for each joint                    |
| pos_curr    | float32[7]      | measured position for each joint                       |
| vel_curr    | float32[7]      | measured velocity for each joint                       |
| torque_curr | float32[7]      | measured torque for each joint                         |
| torque_calc | float32[7]      | calculated torque for each joint by dynamics algorithm |
| e           | float32[7]      | position error computed by dynamics algorithm          |
| e_d         | float32[7]      | velocity error computed by dynamics algorithm          |
