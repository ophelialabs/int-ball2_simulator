#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

def main():
    rospy.init_node("user_node", anonymous=False)
    rospy.spin()

if __name__ == "__main__":
    main()