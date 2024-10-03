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
            'explore = kaiaai_apps.explore:main'
            'param_client_test = kaiaai_apps.param_client_test:main'
        ],
    },
)
