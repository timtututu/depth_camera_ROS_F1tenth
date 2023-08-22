#! /usr/bin/env python 
import rospy
from nav_msgs.msg import Odometry
from actionlib_msgs.msg import GoalID
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Pose, Twist, Transform, TransformStamped



def callback(pos_now):
        #x-direction
        goal=Odometry()

        goal=pos_now
        goal.child_frame_id='base_footprint'
        goal.header.frame_id='odom'
        upd_pos_pub.publish(goal)





def pub_odom(): 
        
    global now_pos_sub,upd_pos_pub,times
    rospy.init_node('pub_odom')
    now_pos_sub = rospy.Subscriber('/vins_node/odometry', Odometry, callback)
    upd_pos_pub=rospy.Publisher('odom',Odometry,queue_size=1)
    rospy.spin()
        

# Start the node
if __name__ == '__main__':
    pub_odom()
