import json

from flask import Blueprint, g, request
from flask_restful import Api, Resource

from .schemas.workout import WorkoutSchema
from whiteboard.models import Workout

workouts_blueprint = Blueprint('workouts', __name__)
workouts_api = Api(workouts_blueprint)


class WorkoutResource(Resource):

    def post(self):
        serialized_workout = request.get_json()
        workout = Workout(activity_type=serialized_workout['activity_type'])
        g.repositories.workouts.store(workout)
        result = WorkoutSchema().dump(workout).data
        return result, 201

    def get(self):
        workouts = g.repositories.workouts.get_all()
        result = WorkoutSchema(many=True).dump(workouts).data
        return json.dumps(
            {'items': result}
        )

workouts_api.add_resource(WorkoutResource, '/workouts')
