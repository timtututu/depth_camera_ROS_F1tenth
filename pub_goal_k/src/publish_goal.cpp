#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>

typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

int main(int argc, char** argv){
  ros::init(argc, argv, "simple_navigation_goals");

  //tell the action client that we want to spin a thread by default
  MoveBaseClient ac("move_base", true);

  //wait for the action server to come up
  while(!ac.waitForServer(ros::Duration(5.0))){
    ROS_INFO("Waiting for the move_base action server to come up");
  }

  move_base_msgs::MoveBaseGoal goal;

  goal.target_pose.header.frame_id = "map"; //"map" for global frame. "base_link" for local frame;
  goal.target_pose.header.stamp = ros::Time::now();

  goal.target_pose.pose.position.x = 10.0;
  goal.target_pose.pose.position.y = 0.0;
  goal.target_pose.pose.orientation.w = 1.0; //Quaternion
  ROS_INFO("Sending goal 1");
  ac.sendGoalAndWait(goal, ros::Duration(50.0,0), ros::Duration(50.0,0));
	
  if(ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
    ROS_INFO("Goal arrived!");
  else
    ROS_INFO("The base failed to move to goalfor some reason");	
	
  goal.target_pose.pose.position.x =15.0;
  goal.target_pose.pose.position.y = 0.0;
  goal.target_pose.pose.orientation.w = 1.0;
  ROS_INFO("Sending goal 2");
  ac.sendGoalAndWait(goal, ros::Duration(60.0,0), ros::Duration(60.0,0));

  if(ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
    ROS_INFO("Goal arrived!");
  else
    ROS_INFO("The base failed to move to goalfor some reason");

  goal.target_pose.pose.position.x = 20.0;
  goal.target_pose.pose.position.y = 0.0;
  goal.target_pose.pose.orientation.w = 1.0;
  ROS_INFO("Sending goal 3");
  ac.sendGoalAndWait(goal, ros::Duration(20.0,0), ros::Duration(20.0,0));

  if(ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
    ROS_INFO("Goal arrived!");
  else
    ROS_INFO("The base failed to move to goalfor some reason");

  return 0;
}
//max=50