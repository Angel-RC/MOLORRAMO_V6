# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   os import environ
import pymysql

class Config(object):

    basedir    = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'key'

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://qado842:Molorramo20@qado842.molorramo.com/qado842?charset=utf8mb4'

    # For 'in memory' database, please use:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
            
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('APPSEED_DATABASE_USER', 'wexblshovbqplg'),
        environ.get('APPSEED_DATABASE_PASSWORD', 'd2f882c81122eecf11e18c38d45dd07fc0edb3e577f2870429f75a8f9446d1c2'),
        environ.get('APPSEED_DATABASE_HOST', 'ec2-54-217-206-236.eu-west-1.compute.amazonaws.com'),
        environ.get('APPSEED_DATABASE_PORT', 5432),
        environ.get('APPSEED_DATABASE_NAME', 'd561hb6caco114')
    )

    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://qado842:Molorramo20@qado842.molorramo.com/qado842?charset=utf8mb4'


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}