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
            'param_client_old = kaiaai_apps.demo.param_client_old:main',
            'param_client = kaiaai_apps.demo.param_client:main',
            'nav_to_pose = kaiaai_apps.demo.nav_to_pose:main',
            'single_goal_nav = kaiaai_apps.demo.single_goal_nav:main',
            'multi_waypoints = kaiaai_apps.demo.multi_waypoints:main',
            'get_map_pos = kaiaai_apps.demo.get_map_pos:main',
            'get_map = kaiaai_apps.demo.get_map:main',
            'load_map = kaiaai_apps.demo.load_map:main',
            'save_map = kaiaai_apps.demo.save_map:main',
            'get_model_params = kaiaai_apps.demo.get_model_params:main',
            'nav_params = kaiaai_apps.demo.nav_params:main',
            'explore_wfe = kaiaai_apps.demo.nav_params:main',
        ],
    },
)
