from flask import Flask
from config import Config
from models import db, bcrypt, jwt
from flask_cors import CORS
from routes import map_bp
from auth import auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(map_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)