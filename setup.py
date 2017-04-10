# coding: utf-8

import os
from setuptools import setup, find_packages


def read_requirements(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        content = f.read()
        return content.split('\n') if content else []


setup(
    name="Whiteboard",
    version="1.0.0",
    author="Bartłomiej Lisiecki",
    author_email="b.m.lisiecki@gmail.com",
    description=("Simple activity journal for personal use."),
    url="http://github.com/bmlis/whiteboard",
    install_requires=read_requirements('requirements.txt'),
    packages=find_packages(exclude=['docs', 'tests*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
