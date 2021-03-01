"""
Define the REST verbs relative to the learning history
"""
from flask import request
from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import learningHistoryRepository
from util import parse_params


class learningHistoryResource(Resource):
    """ Verbs relative to the learning history """

    @staticmethod
    def get():
        learnerData = request.json
        """ Return an learner key information based on his id """
        learnerData = learningHistoryRepository.get(sid=learnerData['studentId'],cid=learnerData['CourseId'],mid=learnerData['ModuleId'])
        return jsonify(learnerData)
