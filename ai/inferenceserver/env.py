import os
from dotenv import load_dotenv


load_dotenv()


DEFAULT_VECTORIZER_PATH = "models/tf_idf_vectorizer.pickle"
DEFAULT_MODEL_PATH = "models/tf_idf_svm_model.pickle"
DEFAULT_THRESHOLD = 0.5
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 4000


VECTORIZER_PATH = (
    os.getenv("HOST") if os.getenv("HOST") is not None else DEFAULT_VECTORIZER_PATH
)
MODEL_PATH = os.getenv("HOST") if os.getenv("HOST") is not None else DEFAULT_MODEL_PATH
THRESHOLD = os.getenv("HOST") if os.getenv("HOST") is not None else DEFAULT_THRESHOLD
HOST = os.getenv("HOST") if os.getenv("HOST") is not None else DEFAULT_HOST
PORT = int(os.getenv("PORT")) if os.getenv("PORT") is not None else DEFAULT_PORT
