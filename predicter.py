from pickle import dump, load
import numpy as np


def load_model(model_filename: str):
    with open(model_filename, 'rb') as file:
        model = load(file)
        return model


def predict(location: int, area: float, year: int, rooms: int, level: int, state: int, model):
    return model.predict([np.array([location, area, year, rooms, level, state])])[0]
