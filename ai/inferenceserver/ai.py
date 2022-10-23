import pickle

from env import VECTORIZER_PATH, MODEL_PATH

with open(VECTORIZER_PATH, "br") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open(MODEL_PATH, "br") as model_file:
    model = pickle.load(model_file)
