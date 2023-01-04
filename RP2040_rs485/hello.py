import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

port='/dev/ttyUSB0'
import serial
ser = serial.Serial(port, 115200,timeout=0.05) 

CMD_SET_VOLTAGE_1 = 101
CMD_SET_VOLTAGE_2 = 102
CMD_READ_VOLTAGE_1 = 111
CMD_READ_VOLTAGE_2 = 112

BOARD_ID = 1

class RS485Node(Node):
    def __init__(self):
        super().__init__('RS485_node')
        self.pub = self.create_publisher(String, 'topic', 10)
        self.sub = self.create_subscription(Int32, 'V1',self.sub_V1_callback,10)
        self.sub = self.create_subscription(Int32, 'V2',self.sub_V2_callback,10)
        self.timer = self.create_timer(0.3, self.timer_callback)
        self.v1=0
        self.dir1=1
        self.v2=0
        self.dir2=1

    def sub_V1_callback(self, msg):
        self.v1=msg.data
        ser.write(b'\x01')
        ser.write(CMD_SET_VOLTAGE_1.to_bytes(1,'big')) #111
        ser.write(self.v1.to_bytes(1, 'big')) #30 bytes(self.v)

        self.get_logger().info(f'SetVoltage1:v={self.v1} ')

    def sub_V2_callback(self, msg):
        self.v2=msg.data
        ser.write(b'\x01')
        ser.write(CMD_SET_VOLTAGE_2.to_bytes(1,'big')) #111
        ser.write(self.v2.to_bytes(1, 'big')) #30 bytes(self.v)
        self.get_logger().info(f'SetVoltage2:v={self.v2} ')


    def timer_callback(self):
        '''
        v_max=50
        if self.dir>0:
            if self.v<v_max:
                self.v=self.v+self.dir
            elif self.v>=v_max:
                self.dir=-1
        if self.dir<0:
            if self.v>0:
                self.v=self.v+self.dir
            elif self.v<=0:
                self.dir=1
        '''

        ser.write(b'\x01')
        ser.write(CMD_READ_VOLTAGE_1.to_bytes(1,'big')) #111
        ser.reset_input_buffer()
        aa=ser.readline()
        aa=aa.decode('utf-8').split('HEAD:')[-1]
        aa=aa.split('\r')[0]
        dd=aa.split(',')

        msg = String()
        msg.data=str(dd)
        self.pub.publish(msg)
        self.get_logger().info(f'data:{msg.data} ')

def main():
    print("hello")
    rclpy.init()
    node=RS485Node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    rclpy.shutdown()

if __name__ == "__main__":
    main()