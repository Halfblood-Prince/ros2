from setuptools import setup

package_name = 'ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'teleop_wasd = ros2.teleop_wasd:main',
        ],
    },
)