"""Pylons environment configuration"""
import os

from genshi.template import TemplateLoader
from pylons import config

import serialservice.lib.app_globals as app_globals
import serialservice.lib.helpers
from serialservice.config.routing import make_map

def load_environment(global_conf, app_conf):
    """Configure the Pylons environment via the ``pylons.config``
    object
    """
    # Pylons paths
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths = dict(root=root,
                 controllers=os.path.join(root, 'controllers'),
                 static_files=os.path.join(root, 'public'),
                 templates=[os.path.join(root, 'templates')])

    # Initialize config with the basic options
    config.init_app(global_conf, app_conf, package='serialservice', paths=paths)

    config['routes.map'] = make_map()

    config['pylons.paths']['data'] = os.path.join(root, 'data') # eerst deze, de volgende lijn initialiseerd app_globals, waar het data-paths in gebruikt wordt.
    config['pylons.app_globals'] = app_globals.Globals()
    config['pylons.h'] = serialservice.lib.helpers

    # Create the Genshi TemplateLoader
    config['pylons.app_globals'].genshi_loader = TemplateLoader(
        paths['templates'], auto_reload=True)

    # CONFIGURATION OPTIONS HERE (note: all config options will override
    # any Pylons config options)
