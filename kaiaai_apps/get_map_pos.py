#! /usr/bin/env python3
import rclpy
from kaiaai.util import MapPose


def main(args=None):
  rclpy.init(args=args)

  map_pose = MapPose()

  while(True):
    position = map_pose.get_map_pos_2d()
    print(position)
    rclpy.spin_once(map_pose)

  rclpy.shutdown()

if __name__ == '__main__':
  main()
