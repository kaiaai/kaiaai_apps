import rclpy
from kaiaai.util import ParamClient


def main():
  rclpy.init()

  param_client = ParamClient('/kaiaai_telemetry_node')
  param_name = 'battery.voltage_empty'

  response = param_client.get(param_name)
#  param_client.get_logger().info('Value: %s' % (response.values[0].string_value))
  value = param_client.to_value(response)
  print(value)
  value = value[0]

  param_client.set(param_name, value + 0.1)

  response = param_client.get(param_name)
  print(param_client.to_value(response))

  param_client.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
