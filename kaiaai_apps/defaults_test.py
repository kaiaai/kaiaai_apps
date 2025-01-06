from kaiaai.util import ModelParams

def main():
  model_params = ModelParams().get_params()
  robot_model_name = model_params['robot_model']['name']

  print(robot_model_name)


if __name__ == '__main__':
  main()
