import sqlalchemy as sa
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from app.config import Config
from flask_jwt_extended import JWTManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)



    # Load the rest of the config from Config class
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)  # Initialize JWT
    CORS(app, supports_credentials=True)

    # Register routes
    from app.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
