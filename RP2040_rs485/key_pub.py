import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class RPMDKeyPub(Node):
    def __init__(self):
        super().__init__('RPMDKeyPub_node')
        self.V1pub = self.create_publisher(Int32, 'V1', 10)
        self.V2pub = self.create_publisher(Int32, 'V2', 10)
        self.timer = self.create_timer(0.3, self.timer_callback)
        self.v1=0
        self.v2=0

    def timer_callback(self):
        key = input()
        if key == 'q': # fキーが押されていたら
            self.v1  = self.v1+5
        elif key == 'a':
            self.v1   = self.v1-5
        elif key == 'e':
            self.v2  = self.v2+5
        elif key == 'd':
            self.v2  = self.v2-5
        else:
            self.v1  = 0
            self.v2  = 0

        if self.v1 <0:
            self.v1=0
        if self.v1 >30:
            self.v1=30
        if self.v2 <0:
            self.v2=0
        if self.v2 >30:
            self.v2=30
        
        '''
        if self.v1<30:
            self.v1=self.v1+1
        else:
            self.v1=0
        '''
        msg = Int32()

        msg.data=self.v1
        self.V1pub.publish(msg)
        self.get_logger().info(f'V1:{msg.data} ')
        msg.data=self.v2
        self.V2pub.publish(msg)
        self.get_logger().info(f'V2:{msg.data} ')


def main():
    print("hello")
    rclpy.init()
    node=RPMDKeyPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    rclpy.shutdown()

if __name__ == "__main__":
    main()