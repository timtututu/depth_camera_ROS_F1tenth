#!/usr/bin/env python

import rospy
import tf2_ros
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from tf.transformations import quaternion_from_euler, euler_from_quaternion

def odom_callback(odom_msg):
    try:

        # tf_buffer = tf2_ros.Buffer()
        # tf_listener = tf2_ros.TransformListener(tf_buffer)
        # transform = tf_buffer.lookup_transform("base_footprint", "odom", odom_msg.header.stamp, rospy.Duration(1.0))
        
        tf_broadcaster = tf2_ros.TransformBroadcaster()

        odom_to_base_transform = TransformStamped()
        odom_to_base_transform.header.stamp = odom_msg.header.stamp
        odom_to_base_transform.header.frame_id = "odom"
        odom_to_base_transform.child_frame_id = "base_footprint"
        odom_to_base_transform.transform.translation.x = odom_msg.pose.pose.position.x
        odom_to_base_transform.transform.translation.y = odom_msg.pose.pose.position.z
        odom_to_base_transform.transform.translation.z = 0

        original_orientation = odom_msg.pose.pose.orientation
        qx, qy, qz, qw = original_orientation.x, original_orientation.y, original_orientation.z, original_orientation.w
        roll, pitch, yaw = euler_from_quaternion([qx, qy, qz, qw])  # Convert quaternion to Euler angles
        roll += 4.712388  # Adding 90 degrees in radians
        qx, qy, qz, qw = quaternion_from_euler(roll, pitch, yaw)  # Convert back to quaternion
        odom_to_base_transform.transform.rotation.x = qx
        odom_to_base_transform.transform.rotation.y = qy
        odom_to_base_transform.transform.rotation.z = qz
        odom_to_base_transform.transform.rotation.w = qw

        tf_broadcaster.sendTransform(odom_to_base_transform)

    except rospy.ROSInterruptException:
        pass

def main():
    rospy.init_node('odom_to_base_footprint_transformer')

    rospy.Subscriber('/vins_node/odometry', Odometry, odom_callback)

    rospy.spin()

if __name__ == '__main__':
    main()

