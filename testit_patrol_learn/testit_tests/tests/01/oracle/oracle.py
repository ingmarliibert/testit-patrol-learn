#!/usr/bin/env python

import rospy
import sys
from move_base_msgs.msg import *
from geometry_msgs.msg import PoseStamped


def has_reached_goal(data):
    goal_status = data.status.text
    rospy.loginfo(goal_status)
    if goal_status == "Goal reached.":
        return True
    else:
        return False


def respond_move_base_result(x, y):
    msg_result = rospy.wait_for_message("/robot_0/move_base/result", MoveBaseActionResult)
    if has_reached_goal(msg_result):
        rospy.loginfo("Point x: %f y: %f reached successfully", x, y)
        sys.exit(0)  # success
    else:
        rospy.loginfo("Did not reach point x: %f y: %f", x, y)
        sys.exit(1)  # fail


def respond_goal_success(data, expected_x, expected_y):
    x = float(data.pose.position.x)
    y = float(data.pose.position.y)
    rospy.loginfo('Checking goal status X: %f Y: %f', x, y)

    if expected_x - 0.1 <= x <= expected_x + 0.1 and expected_y - 0.1 <= y <= expected_y + 0.1:
        respond_move_base_result(x, y)
    else:
        rospy.loginfo("Waiting for a next goal")


def oracle():
    rospy.init_node('oracle', anonymous=True)
    rospy.loginfo("Starting oracle ...")
    rate = rospy.Rate(2)

    x, y = list(map(float, sys.argv[1:3]))

    while not rospy.is_shutdown():
        rospy.loginfo("Waiting for goal ...")
        pose = rospy.wait_for_message("/robot_0/move_base_node/current_goal", PoseStamped)
        respond_goal_success(pose, x, y)
        rate.sleep()


if __name__ == '__main__':
    oracle()
