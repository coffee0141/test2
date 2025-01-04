import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main():
    rclpy.init()
    node = Node("listener")

    def callback(msg):
        text = msg.data
        word_count = len(text.split())  
        char_count = len(text)         
        node.get_logger().info(f'Received: "{text}" (Word count: {word_count}, Character count: {char_count})')

    node.create_subscription(String, "chatter", callback, 10)
    rclpy.spin(node)

if __name__ == "__main__":
    main()




