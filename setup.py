from setuptools import find_packages, setup

package_name = 'kaiaai_apps'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='Kaia.ai sample apps',
    author='Ilia O.',
    author_email='iliao@kaia.ai',
    maintainer='Ilia O.',
    maintainer_email='iliao@kaia.ai',
    license='Apache-2.0',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'explore = kaiaai_apps.explore:main',
            'param_client_test = kaiaai_apps.param_client_test:main',
            'demo_param_client = kaiaai_apps.demo_param_client:main',
            'example_nav_to_pose = kaiaai_apps.example_nav_to_pose:main',
            'single_goal_nav = kaiaai_apps.single_goal_nav:main',
            'multi_waypoints = kaiaai_apps.multi_waypoints:main',
            'demo_get_map_pos = kaiaai_apps.demo_get_map_pos:main',
            'demo_get_map = kaiaai_apps.demo_get_map:main',
            'demo_get_model_params = kaiaai_apps.demo_get_model_params:main',
            'nav_params_test = kaiaai_apps.nav_params_test:main',
        ],
    },
)
