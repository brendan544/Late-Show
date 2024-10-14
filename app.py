from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import create_routes
from config import Config

# Initialize Flask extensions
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    create_routes(app)
    return app

# Only for direct execution (not necessary when using Flask CLI)
if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)