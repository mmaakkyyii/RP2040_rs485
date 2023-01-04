from setuptools import setup

package_name = 'RP2040_rs485'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mmaakkyyii',
    maintainer_email='mmaakkyyii@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello = RP2040_rs485.hello:main',
            'key_pub = RP2040_rs485.key_pub:main'
        ],
    },
)
