""" Defines the learning history repository """
import json
from models import Learning_history


class Learning_historyRepository:
    """ The repository for the learning history"""

    @staticmethod
    def get(id):
        """ Query a user by id"""
        learner = Learning_history.query.filter_by(studentid=id).first()
        print(learner)
        learner= dict(studentid=learner.studentid,date=learner.date,age=learner.age,learninghours=learner.learninghours,cpuusage=learner.cpuusage,cost=learner.cost,courseid=learner.courseid,noofmoudles=learner.noofmoudles,maxnoofsubmission=learner.maxnoofsubmission,batchid=learner.batchid)
        return learner
