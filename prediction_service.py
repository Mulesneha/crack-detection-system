import cv2
import numpy as np
from tensorflow.keras.models import load_model
from config import MODEL_PATH

model = load_model(MODEL_PATH)

def preprocess(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.reshape(img, (1, 224, 224, 3))
    return img

def predict_crack(img_path):
    img = preprocess(img_path)
    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        return "Crack Detected", "High"
    else:
        return "No Crack", "Low"