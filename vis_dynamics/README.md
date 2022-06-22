# Visualize Robot Dynamics
Using [`rqt_multiplot`](http://wiki.ros.org/rqt_multiplot), visualize position, torque errors along with input position and velocity errors for Inverse Dynamics.  
Relies on `roahm_msgs/debug` and by default plots topic `/debug`

## Install RQT Multiplot:
```bash
$ sudo apt-get install ros-noetic-rqt-multiplot
```

## Usage:
```bash
$ roslaunch vis_dynamics graph_error.launch
```

## API
see [vis_dynamics](https://roahmlab.github.io/kinova_control/vis_dynamics/html/index.html).
