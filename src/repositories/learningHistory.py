""" Defines the learning history repository """
import json
from flask import jsonify


class learningHistoryRepository:
    """ The repository for the learning history"""

    @staticmethod
    def get(sid,cid,mid):
        """ Query a user by id"""
        l=[]
        #learners = Learning_history.query.all()
        #for learner in learners:
            #print(learner)
            #temp= dict(studentid=learner.studentid,date=learner.date,age=learner.age,learninghours=learner.learninghours,cpuusage=learner.cpuusage,cost=learner.cost,courseid=learner.courseid,noofmoudles=learner.noofmoudles,maxnoofsubmission=learner.maxnoofsubmission,batchid=learner.batchid)
            #print(temp)
            #l.append(temp)
        #print(l)
        ###tester code
        temp=dict(studentid=sid,courseid=cid,moduleid=mid)
        l.append(temp)
        ###tester code end
        return l
