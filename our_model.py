from keras.models import Sequential
from keras.layers import Dense
import pickle
import numpy as np
import os

def build_model():
    model = Sequential()
    model.add(Dense(2, input_shape=(1,)))
    model.add(Dense(1))
    model.summary()
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["acc"])

    return model

def train_save_model(model, X,y, path):
    model.fit(X,y)
    pickle.dump(model, open(path, "wb"))

def generate_data():
    X = np.asarray([1,1,1,1])
    y = np.asarray([0,0,0,0])
    return X,y

def load_trained_model():
    """ Load model a global model instance, return it's pointer."""
    global model
    model = pickle.load(open(os.path.join(os.path.dirname(__file__), "model-v0.1.pkl"), "rb"))
    model._make_predict_function()  # have to initialize before threading
    return model

def main():
    model = build_model()
    X,y = generate_data()
    train_save_model(model,X,y, "model-v0.1.pkl")

if __name__ == "__main__":
    main()