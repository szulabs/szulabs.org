from flask import Flask
from flask.ext.gears import Gears

from szulabs.assets import setup_assets_compilers, setup_assets_compressors
from szulabs.views.master import master_app
from szulabs.views.people import people_app
from szulabs.views.team import team_app
from szulabs.views.experiments import experiments_app


#: flask extensions
gears = Gears()


def create_app(import_name=None, config=None):
    """Creates an application instance."""
    app = Flask(import_name or __name__)

    app.config.from_object("szulabs.settings")
    app.config.from_pyfile(config)

    gears.init_app(app)
    setup_assets_compilers(app)
    setup_assets_compressors(app)

    app.register_blueprint(master_app)
    app.register_blueprint(people_app)
    app.register_blueprint(team_app)
    app.register_blueprint(experiments_app)

    return app
