import rclpy
from kaiaai.util import ParamClient
from kaiaai.util import ModelParams


def main():
  defaults = ModelParams().get_params()

  rclpy.init()

  # ros2 node list
  # ros2 param list /controller_server
  # ros2 param get /controller_server FollowPath.xy_goal_tolerance
  # ros2 param set /controller_server FollowPath.xy_goal_tolerance 0.05
  controller_server = ParamClient('/controller_server')

  param_name = 'FollowPath.xy_goal_tolerance'
  response = controller_server.get(param_name)
#  param_client.get_logger().info('Value: %s' % (response.values[0].string_value))
  value = controller_server.to_value(response)
  # print('Get', param_name, value)
  # value = value[0]

  default_value = defaults['robot_model']['follow_path']['xy_goal_tolerance']['mapping']
  controller_server.set(param_name, default_value)

  response = controller_server.get(param_name)
  print(param_name, controller_server.to_value(response), '->', value)


  param_name = 'FollowPath.max_vel_x'
  response = controller_server.get(param_name)
  value = controller_server.to_value(response)
  # print('Get', param_name, value)
  # value = value[0]

  default_value = defaults['robot_model']['follow_path']['vel_x']['mapping']
  controller_server.set(param_name, default_value)

  response = controller_server.get(param_name)
  print(param_name, controller_server.to_value(response), '->', value)


  controller_server.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()
