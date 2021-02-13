# https://flask.palletsprojects.com/en/1.1.x/patterns/packages/

from setuptools import setup

setup(
    name='hello_app',
    packages=['hello_app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)