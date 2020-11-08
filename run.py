# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from os import environ
from sys import exit

from flask_marshmallow import Marshmallow

from config import config_dict
from app import create_app, db

get_config_mode = environ.get('APPSEED_CONFIG_MODE', 'Production')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid APPSEED_CONFIG_MODE environment variable entry.')

app = create_app(config_mode) 
ma = Marshmallow(app)
Migrate(app, db)

if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run()
