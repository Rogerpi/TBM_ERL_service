#!/usr/bin/env python

#Author: Roger Pi Roig

import rospy
import numpy as np
import math
import copy
import sys

from robot_map.srv import SemanticGoal, SemanticGoalResponse

class tbm1:
    def __init__(self):
        self.phase = 0
        # Define Publishers

        # Define Subscribers
        self.change_phase_sub = rospy.Subscriber('/tbm1/change_phase',String,self.change_phase_callback)
        self.put_object_back_sub = rospy.Subscriber('/tbm1/send_back_to_place',String,self.place_object_default_callback)
        # Define service calls

        # Define service handle

        print("Load semantic from param...")
        load_semantic_from_param = rospy.ServiceProxy('/semantic_map/load_from_param', Empty)
        load_semantic_from_param()
        print("Done!")

    def phase1(self):
        self.phase = 1

        print("Init Survey...")
        call_survey = rospy.ServiceProxy('/semantic_map/follow_path',SemanticGoal)
        survey = SemanticGoal()
        survey.goal_name = "SurveyTBM1"
        call_survey(survey)

        # TODO : restart map. Call god knows how to run perception. Send survey request

    def phase2(self):
        self.phase = 2
        # Send Stop survey request

        #
    def phase3(self):
        self.phase = 3
        save_map = rospy.ServiceProxy('/semantic_map/save_map', Empty)
        save_map()
        print("END TBM1")
        rospy.signal_shutdown('Quit')
        # Request outputs



    def change_phase_callback(self,msg):
        if "1" in msg.data:
            self.phase1()
        elif "2" in msg.data:
            self.phase2():
        elif "3" in msg.data:
            self.phase3():
        elif "next":
            if self.phase == 0:
                self.phase1()
            elif self.phase == 1:
                self.phase2()
            elif self.phase == 2:
                self.phase3()
            else:
                print("Hello bug! :) (Node should have stopped already)")
        else:
            print("Wrong call")

    def place_object_default_callback(self,data):
        print("Send back to position "+str(data.msg))
        pass

if __name__ == '__main__':

    # ROS initializzation
    rospy.init_node('tbm1', anonymous=False)


    node = tbm1()
    rospy.spin()

    #r = rospy.Rate(10)
    #while not rospy.is_shutdown():
    #    r.sleep()
    #    node.publish()

    #Using timer instead of rate for more accurate timing response (inside Semantic Map)
