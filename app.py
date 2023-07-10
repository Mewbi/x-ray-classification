from flask import Flask
from routes import routes
from utils import ia
import config

app = Flask(__name__)

app.register_blueprint(routes.user_bp)
app.register_blueprint(routes.image_bp)
app.register_blueprint(routes.general_bp)

if __name__ == "__main__":
    ia.load(app)
    config.load(app)
    app.run()
