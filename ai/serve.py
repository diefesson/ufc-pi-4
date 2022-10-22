import pickle as pk
from time import sleep
import flask
import pytest
import multiprocessing
import requests

VECTORIZER_PATH = "models/tf_idf_vectorizer.pickle"
MODEL_PATH = "models/tf_idf_svm_model.pickle"

THRESHOLD = 0.5
NOT_OFFENSIVE_LABEL = "NOT_OFFENSIVE"
OFFENSIVE_LABEL = "OFFENSIVE"

HOST = "127.0.0.1"
PORT = "4000"

with open(VECTORIZER_PATH, "br") as vectorizer_file:
    VECTORIZER = pk.load(vectorizer_file)

with open(MODEL_PATH, "br") as model_file:
    MODEL = pk.load(model_file)


app = flask.Flask(__name__)


@app.get("/")
def service():
    comment = flask.request.args["comment"]
    result = MODEL.predict_proba(VECTORIZER.transform([comment]))
    not_offensive_prob, offensive_prob = result[0]
    classification = (
        OFFENSIVE_LABEL if offensive_prob > THRESHOLD else NOT_OFFENSIVE_LABEL
    )
    return {
        "not_offensive_prob": not_offensive_prob,
        "offensive_prob": offensive_prob,
        "classification": classification,
    }


def serve(host, port):
    app.run(host=host, port=port)


def main():
    serve(HOST, PORT)


@pytest.fixture(autouse=True, scope="session")
def setup_server():
    """Setups server for endpoint testing"""
    server_process = multiprocessing.Process(target=serve, args=(HOST, PORT))
    server_process.start()
    # Awaits for server to start
    sleep(5)
    yield
    server_process.terminate()


def test_server():
    res = requests.get(
        f"http://{HOST}:{PORT}",
        params={
            "comment": "welcome to Narnia",
        },
    )
    assert res.status_code == 200


if __name__ == "__main__":
    main()
