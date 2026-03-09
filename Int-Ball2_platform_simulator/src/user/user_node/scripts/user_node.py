#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

class UserTemplate:

    MAX_MSG_SIZE = 800

    def __init__(self):
        rospy.init_node('user_node', anonymous=False)
        self.__rate = rospy.Rate(1)

    def run(self):
        while not rospy.is_shutdown():
            self.__rate.sleep()

if __name__ == '__main__':
    UserTemplate().run()