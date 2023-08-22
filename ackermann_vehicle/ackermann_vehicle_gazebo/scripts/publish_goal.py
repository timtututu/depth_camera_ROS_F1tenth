#!/usr/bin/env python
#-*-coding:utf-8-*-

import rospy
from nav_msgs.msg import Odometry
from actionlib_msgs.msg import GoalID
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Pose, Twist, Transform, TransformStamped
from gazebo_msgs.msg import LinkStates
from std_msgs.msg import Header
from rosgraph_msgs.msg import Clock
import numpy as np
import math
import tf2_ros
times=0; seq_g=1 ;goal_p=PoseStamped()


def callback(time_now):
        global times, seq_g,goal_p
        #x-direction
        goal=PoseStamped()
        present_time=Clock()
        
        #pos_now=Odometry()
        if times==0 and int(time_now.clock.secs)>=15:
             goal.header.stamp.secs=int(time_now.clock.secs)
             goal.header.stamp.nsecs=int(time_now.clock.nsecs)
             goal.header.seq=seq_g
             goal.header.frame_id='map'
             goal.pose.position.x=5
             goal.pose.position.y=0
             goal.pose.position.z=0
             goal.pose.orientation.x=0
             goal.pose.orientation.w=1
             goal.pose.orientation.y=0
             goal.pose.orientation.z=0
             times+=1; seq_g+=1
             goal_p=goal
             rospy.loginfo('ininin')
             upd_pos_pub.publish(goal_p)
        # else:
        #     a=pos_now.pose.pose.position.x

        

        





def pub_new_goal(): 
        
    global now_pos_sub,upd_pos_pub,times
    rospy.init_node('pub_goal')
    now_time_sub = rospy.Subscriber('/clock', Clock, callback)
    #now_pos_sub = rospy.Subscriber('/odom', Odometry, callback)
    upd_pos_pub=rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=1)
    rospy.spin()
        

# Start the node
if __name__ == '__main__':
    pub_new_goal()
