import os
import numpy as np
import matplotlib.pyplot as plt 
from cv2 import cv2
import pickle

data_dir = './data/flowers' 

categories = ['daisy', 'sunflower','rose', 'tulip','dandelion']

data = []

def build_data():
    for category in categories:
        path = os.path.join(data_dir,category)
        label = categories.index(category)

        for img_name in os.listdir(path):
            image_path = os.path.join(path, img_name)
            image = cv2.imread(image_path)

            try:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image,(224,224))
                image = np.array(image, dtype=np.float32)
                data.append([image, label])

            except Exception as e :
                     pass

        print(len(data))

        pik = open('data.pickle', 'wb')
        pickle.dump(data, pik)
        pik.close()

build_data()

def load_data():
    pick = open('data.pickle', 'rb')
    data = pickle.load(pick)
    pick.close()

    np.random.shuffle(data)

    feature = []
    labels = []

    for img, label in data:
        feature.append(img)
        labels.append(label)

    feature = np.array(feature, dtype=np.float32)
    labels = np.array(labels)

    feature = feature/255.0

    return[feature, labels]