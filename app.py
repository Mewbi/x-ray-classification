from flask import Flask
from routes import routes

app = Flask(__name__)

app.register_blueprint(routes.user_bp)
app.register_blueprint(routes.image_bp)

if __name__ == '__main__':
    app.run()
