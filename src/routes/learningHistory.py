from flask import Blueprint
from flask_restful import Api

from resources import learningHistoryResource

LEARNING_HISTORY_BLUEPRINT = Blueprint("learningHistory", __name__)
Api(LEARNING_HISTORY_BLUEPRINT).add_resource(
    learningHistoryResource, "/api/v1/platformServices/learningHistory/"
)
