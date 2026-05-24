from flask import Blueprint
from controllers.detect_controller import detect_crack_controller

detect_bp = Blueprint('detect', __name__)

@detect_bp.route('/detect', methods=['POST'])
def detect():
    return detect_crack_controller()