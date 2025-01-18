#! /usr/bin/env python3
import rclpy
from kaiaai.util import NavUtils


def main(args=None):
  rclpy.init(args=args)

  nav_utils = NavUtils()
  position = nav_utils.getMapPos2d()
  print(position)

  rclpy.shutdown()

if __name__ == '__main__':
  main()
