# -*- coding: utf-8 -*-
from flask import Blueprint

public = Blueprint('public', __name__)


@public.route("/")
def hello():
    return 'Hello World'
