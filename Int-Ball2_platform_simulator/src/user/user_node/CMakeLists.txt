cmake_minimum_required(VERSION 3.0.2)
project(user_node)

find_package(catkin REQUIRED)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/user_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)