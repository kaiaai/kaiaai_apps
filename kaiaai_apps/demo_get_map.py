#! /usr/bin/env python3
import rclpy
from kaiaai.util import NavUtils, OccupancyGrid2d


def main(args=None):
  rclpy.init(args=args)

  nav_utils = NavUtils()

  map = nav_utils.getCurrentMap()
  print(map.map)

  rclpy.shutdown()

if __name__ == '__main__':
  main()
