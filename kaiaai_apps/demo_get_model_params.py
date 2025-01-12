#! /usr/bin/env python3
import rclpy
from kaiaai.util import NavUtils


def main(args=None):

  model_params = ModelParams.get_params()
  print(model_params)

  robot_model_name = model_params['robot_model']['name']
  print(robot_model_name)


if __name__ == '__main__':
  main()
