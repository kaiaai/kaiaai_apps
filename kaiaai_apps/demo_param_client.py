#! /usr/bin/env python3
import rclpy
from rclpy.parameter import Parameter
# https://github.com/ros2/rclpy/blob/rolling/rclpy/rclpy/parameter_client.py


def main():
  rclpy.init()

  node = rclpy.create_node('my_node')
  client = AsyncParameterClient(node, 'example_node')

  # set parameters on example node
  future = client.set_parameters([
    Parameter('int_param', Parameter.Type.INTEGER, 88),
    Parameter('string/param', Parameter.Type.STRING, 'hello world').to_parameter_msg(),
  ])
  self.executor.spin_until_future_complete(future)
  results = future.result()  # rcl_interfaces.srv.SetParameters.Response

  node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()
