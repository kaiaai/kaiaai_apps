#! /usr/bin/env python3
import rclpy
from kaiaai.util import NavUtils


def main(args=None):
  rclpy.init(args=args)

  nav_utils = NavUtils()

  model_params = ModelParams().get_params()
  print(model_params)

  robot_model_name = model_params['robot_model']['name']
  print(robot_model_name)

  while(True):
    position = nav_utils.getMapPos2d()
    print(position)
    rclpy.spin_once(nav_utils)

  rclpy.shutdown()

if __name__ == '__main__':
  main()
