import os
from flask import request, jsonify
from services.prediction_service import predict_crack
from models.db_model import collection
from config import UPLOAD_FOLDER
from datetime import datetime

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def detect_crack_controller():
    file = request.files['image']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result, severity = predict_crack(path)

    data = {
        "filename": file.filename,
        "result": result,
        "severity": severity,
        "time": datetime.now()
    }

    collection.insert_one(data)

    return jsonify(data)