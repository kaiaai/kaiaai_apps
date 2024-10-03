from kaiaai.util import ParamClient


def main():
  rclpy.init()

  param_client = ParamClientAsync('/kaiaai_telemetry')

  response = param_client.get(['my_parameter', 'your_parameter'])
  param_client.get_logger().info(
    'First value: %s, Second value: %s' %
    (response.values[0].string_value, response.values[1].string_value))

  param_client.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
