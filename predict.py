import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# تحميل النموذج
model = load_model("keras_model.h5")

# تحميل أسماء الأصناف من labels.txt
def load_labels(path="labels.txt"):
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]

class_names = load_labels()

# التنبؤ بالصورة
def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    class_name = class_names[class_index]
    confidence = prediction[0][class_index]

    print(f"✅ Prediction: {class_name} (Confidence: {confidence:.2f})")

# شغل البرنامج
if name == "__main__":
    predict("test.jpg")