from flask import Flask
def create_app(config_name):
    app = flask(__name__)
    return app