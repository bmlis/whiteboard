import os
from setuptools import setup, find_packages

setup(
    name="Whiteboard",
    version="1.0.0",
    author="Bartłomiej Lisiecki",
    author_email="b.m.lisiecki@gmail.com",
    description=("Simple activity journal for personal use."),
    url="http://github.com/bmlis/whiteboard",
    packages=find_packages(exclude=['docs', 'tests*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
