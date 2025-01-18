#! /usr/bin/env python3
# Copyright 2021 Samsung Research America
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from rclpy.duration import Duration
from kaiaai.explore.wfd import WavefrontFrontierDetector
from kaiaai.util import NavUtils


def main():
  rclpy.init()

  navigator = BasicNavigator()
  explorer = WavefrontFrontierDetector()
  navigator.waitUntilNav2Active(localizer='bt_navigator') # hack

  nav_utils = NavUtils()

  while True:
    map = nav_utils.getCurrentMap()
    navigator.info('Got current map')
    # print(map.map)

    position = nav_utils.getMapPos()
    navigator.info('Got current position on the map')

    goal = explorer.getNextGoal(position, map)

    if goal == None:
      navigator.info('No More Frontiers')
      break

    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = goal.x
    goal_pose.pose.position.y = goal.y
    goal_pose.pose.orientation.w = 0.0

    # sanity check a valid path exists
    # path = navigator.getPath(initial_pose, goal_pose)

    navigator.goToPose(goal_pose)

    i = 0
    while not navigator.isTaskComplete():
      i = i + 1
      feedback = navigator.getFeedback()
      if feedback and i % 10 == 0:
        print('Estimated time of arrival: ' + '{0:.0f}'.format(
          Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9) + ' seconds.')

      # Some navigation timeout to demo cancellation
      if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
        navigator.cancelTask()

    result = navigator.getResult()
    navigator.info(nav_utils.taskResultToText(result))

# navigator.lifecycleShutdown()

  exit(0)


if __name__ == '__main__':
  main()
