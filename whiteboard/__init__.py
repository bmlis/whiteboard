# -*- coding: utf-8 -*-
from flask import Flask
from whiteboard.controllers import public


app = Flask(__name__)
app.register_blueprint(public)