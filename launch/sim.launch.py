from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():

    pkg = os.path.join(os.getenv('HOME'),'ros2_pro_ws/src/ros2')

    return LaunchDescription([

        ExecuteProcess(
            cmd=['gazebo','--verbose', pkg+'/worlds/env.world','-s','libgazebo_ros_factory.so'],
            output='screen'
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity','cuboid_bot','-file',pkg+'/urdf/cuboid_bot.urdf'],
            output='screen'
        ),

        Node(
            package='ros2',
            executable='teleop_wasd'
        )
    ])
