# -*- coding: utf-8 -*-
from flask import Flask, g
from flask_cors import CORS

from whiteboard.controllers import public
from whiteboard.controllers.workouts import workouts_blueprint
from whiteboard.repositories import Repositories


class ApplicationContext:
    def __init__(self):
        self.repositories = Repositories()


def create_app(context, debug=False):
    app = Flask(__name__)
    CORS(app)

    @app.before_request
    def before_request():
        g.repositories = context.repositories

    app.register_blueprint(public)
    app.register_blueprint(workouts_blueprint)
    return app
