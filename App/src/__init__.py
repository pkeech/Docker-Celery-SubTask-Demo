## Import Required Modules
#from .extensions import db, login_manager, sess, debug_toolbar, babel, migrate
from flask import Flask, flash, redirect, url_for

## [FOR DOCKER PURPOSES] Redirect Logs to STDOUT
import logging, os
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

## Define Flask Application
def create_app(settings_override=None):
    ## Create Application
    app = Flask(__name__)

    ## Initialize Extenstions
    extensions(app)

    ## Create Application Context
    with app.app_context():
        ## Define Routes
        @app.route("/")
        def index():
            return "HELLO WORLD!"

        ## Handle Logging
        app.logger.addHandler(stream_handler)

        ## Return Application
        return app

## Load (Stage) Flask Extensions
def extensions(app):
    ## Initialize Flask-SQLAlchemy
    #db.init_app(app)   
    
    return None