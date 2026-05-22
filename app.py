from flask import Flask
from flask_cors import CORS
from routes.detect_routes import detect_bp
from routes.history_routes import history_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(detect_bp)
app.register_blueprint(history_bp)

if __name__ == "__main__":
    app.run(debug=True)