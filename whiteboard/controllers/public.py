# -*- coding: utf-8 -*-
from flask import Blueprint

public = Blueprint('frontend', __name__)


@public.route("/")
def hello():
    return 'Hello World'
