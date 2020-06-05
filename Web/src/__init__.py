## Import Required Modules
#from .extensions import db, login_manager, sess, debug_toolbar, babel, migrate
from flask import Flask, flash, redirect, url_for
from celery import Celery

## [FOR DOCKER PURPOSES] Redirect Logs to STDOUT
import logging, os
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

## DEFINE FLASK APPLICATION
def create_app(settings_override=None):
    ## Create Application
    app = Flask(__name__)

    ## Initialize Extenstions
    extensions(app)

    ## INSTANTIATE CELERY APP
    celeryapp = Celery(broker=os.environ.get("CELERY_BROKER_URL", default="redis://:Pa55w0rd!@redis:6379/0"))
    celeryapp.config_from_object('src.celeryconfig')

    ## Create Application Context
    with app.app_context():
        ## Define Routes
        @app.route("/")
        def index():
            return "HELLO WORLD!"

        @app.route("/task1")
        def task1():
            r = celeryapp.send_task('tasks.task1')
            return r.id

        @app.route("/parent")
        def parent():
            r = celeryapp.send_task('tasks.parent')
            return r.id

        ## Handle Logging
        app.logger.addHandler(stream_handler)

        ## Return Application
        return app

## Load (Stage) Flask Extensions
def extensions(app):
    ## Initialize Flask-SQLAlchemy
    #db.init_app(app)   
    
    return None