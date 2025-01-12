#! /usr/bin/env python3
import rclpy
from kaiaai.util import NavUtils


def main(args=None):
  rclpy.init(args=args)

  nav_utils = NavUtils()

  while(True):
    position = nav_utils.getMapPos2d()
    print(position)
    rclpy.spin_once(nav_utils)

  rclpy.shutdown()

if __name__ == '__main__':
  main()
