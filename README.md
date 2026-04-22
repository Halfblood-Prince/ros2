# ROS2 Cuboid Bot Workspace

Cuboid robot in Gazebo with LiDAR, WASD control, and SLAM-ready setup.

## Setup Instructions

### Clone the repository
```bash
cd ~
git clone <your-repo-url> ros2_ws
cd ros2_ws
```

### Build the workspace
```bash
colcon build
```

### Source the environment
```bash
source install/setup.bash
```

### Run the simulation
```bash
ros2 launch ros2 sim.launch.py
```

## Package Contents

- **package**: ROS2 ament_python package with WASD keyboard control
- **URDF**: Cuboid robot model with LiDAR sensor
- **Gazebo World**: Simple room environment with ground plane
- **Launch File**: Starts Gazebo, spawns the robot, and launches teleop node

## Dependencies

- rclpy
- geometry_msgs
- gazebo_ros
- gazebo_plugins
- robot_state_publisher
- joint_state_publisher
- xacro
- rviz2

Install them via rosdep:
```bash
rosdep install --from-paths src --ignore-src -r -y
```
