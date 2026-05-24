from flask import Blueprint
from controllers.history_controller import get_history_controller

history_bp = Blueprint('history', __name__)

@history_bp.route('/history', methods=['GET'])
def history():
    return get_history_controller()