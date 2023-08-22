#!/usr/bin/env python

import rospy
import tf2_ros
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped

def odom_callback(odom_msg):
    try:
        tf_broadcaster = tf2_ros.TransformBroadcaster()

        odom_to_base_transform = TransformStamped()
        odom_to_base_transform.header.stamp = odom_msg.header.stamp
        odom_to_base_transform.header.frame_id = "odom"
        odom_to_base_transform.child_frame_id = "base_footprint"
        odom_to_base_transform.transform.translation.x = odom_msg.pose.pose.position.x
        odom_to_base_transform.transform.translation.y = odom_msg.pose.pose.position.y
        odom_to_base_transform.transform.translation.z = odom_msg.pose.pose.position.z
        odom_to_base_transform.transform.rotation = odom_msg.pose.pose.orientation


        tf_broadcaster.sendTransform(odom_to_base_transform)

    except rospy.ROSInterruptException:
        pass

def main():
    rospy.init_node('odom_to_base_footprint_transformer')

    rospy.Subscriber('/vesc/odom', Odometry, odom_callback)

    rospy.spin()

if __name__ == '__main__':
    main()
