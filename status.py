#!/usr/bin/env python3
import rospy
from tello_driver.msg import TelloStatus

def callback(data):
    rospy.loginfo("Height: " + str(data.height_m))
    rospy.loginfo("Battery Percentage: " + str(data.battery_percentage))
    rospy.loginfo("Flight Time: " + str(data.flight_time_sec))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/tello/status", TelloStatus, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()