# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():
    
    #if not current_user.is_authenticated:
    #    return redirect(url_for('base_blueprint.login'))

    return render_template('index.html')

@blueprint.route('/<template>')
def route_template(template):

    #if not current_user.is_authenticated:
    #    return redirect(url_for('base_blueprint.login'))

    try:

        # Flexible rendering 
        # Sample pattern: '/profile' AND '/profile.html' 
        if not template.endswith( '.html' ):
            template += '.html'

        return render_template(template)

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500
