from setuptools import setup

package_name = 'ros2'

setup(
    name=package_name,
    version='0.0.1',
    packages=['ros2'],
    entry_points={
        'console_scripts': [
            'teleop_wasd = ros2.teleop_wasd:main',
        ],
    },
)
