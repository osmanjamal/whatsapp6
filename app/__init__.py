from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.whatsapp.webhook import whatsapp as whatsapp_blueprint
    app.register_blueprint(whatsapp_blueprint, url_prefix='/whatsapp')

    from app.admin.views import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app

from app import models  # Import models to ensure they are known to Flask-Migrate