#!/usr/bin/env python
from __future__ import print_function
import time

import serial
import rospy
from geometry_msgs.msg import Twist

from BGT24LTR11.BGT24LTR11 import Radar


def init_radar():
    serial_ = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=2)
    radar = Radar(serial_, verbose=False)
    radar.set_detection_threshold(2500)
    radar.set_mode_target()

    return radar


if __name__ == "__main__":
    rospy.init_node('radar_ADAS')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=0)

    radar = init_radar()

    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        info = radar.get_target_info()
        msg = Twist()
        if info['state'] == 2:
            msg.linear.x = 0
            msg.angular.y = 0

            pub.publish(msg)
            time.sleep(0.2)
        else:
            msg.linear.x = 0.15
            msg.angular.y = 0

            pub.publish(msg)

        rate.sleep()
