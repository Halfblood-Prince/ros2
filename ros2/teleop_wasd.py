import rclpy
from geometry_msgs.msg import Twist
import sys, termios, tty

def get_key():
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return ch

def main():
    rclpy.init()
    node = rclpy.create_node('teleop_wasd')
    pub = node.create_publisher(Twist, 'cmd_vel', 10)

    print("WASD control (W/S forward/back, A/D rotate)")

    while rclpy.ok():
        key = get_key()
        msg = Twist()

        if key == 'w':
            msg.linear.x = 0.6
        elif key == 's':
            msg.linear.x = -0.6
        elif key == 'a':
            msg.angular.z = 1.2
        elif key == 'd':
            msg.angular.z = -1.2
        else:
            continue

        pub.publish(msg)

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    main()
