from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import cv2
import numpy as np


names = '''airplane automobile bird cat deer dog frog horse ship truck'''.split()
model = load_model("models/cifar-10.h5")

# Process image and predict label


def processImg(IMG_PATH):
    # Preprocess image
    image = cv2.imread(IMG_PATH)
    image = cv2.resize(image, (32, 32))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    res = model.predict(image)

    label = np.argmax(res)
    labelName = names[label]
    print("The image is of ", labelName)
    print("confidence: ", np.max(res))

    ret = dict()
    ret['label'] = labelName
    ret['confidence'] = str(np.max(res))
    return ret
