import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

def main():
    rclpy.init()
    node = Node("talker")
    publisher = node.create_publisher(String, "chatter", 10)

    sentences = [
        "Hello world!",
        "I have a pen.",
        "Do you like apple?",
        "Thank you.",
        "My name is Haru Motoyama."
    ]

    def timer_callback():
        msg = String()
        msg.data = random.choice(sentences)  
        node.get_logger().info(f'Publishing: "{msg.data}"')
        publisher.publish(msg)

    node.create_timer(1.0, timer_callback)  
    rclpy.spin(node)

if __name__ == "__main__":
    main()



