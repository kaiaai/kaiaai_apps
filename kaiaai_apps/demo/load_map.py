#! /usr/bin/env python3
import rclpy
from kaiaai.util import NavUtils, OccupancyGrid2d


def main(args=None):

  map = OccupancyGrid2d.load('/ros_ws/map.png')
  print(map.map)

if __name__ == '__main__':
  main()
