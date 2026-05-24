from flask import jsonify
from models.db_model import collection

def get_history_controller():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)