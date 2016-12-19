import json

from flask import Blueprint, g, request
from flask_restful import Api, Resource

from whiteboard.models import Workout

workouts_blueprint = Blueprint('workouts', __name__)
workouts_api = Api(workouts_blueprint)


class WorkoutResource(Resource):

    def post(self):
        serialized_workout = request.get_json()
        workout = Workout(activity_type=serialized_workout['activity_type'])
        g.repositories.workouts.store(workout)
        return 'Hello?', 201

    def get(self):
        return json.dumps([m.activity_type for m in g.repositories.workouts.get_all()])

workouts_api.add_resource(WorkoutResource, '/workouts')
