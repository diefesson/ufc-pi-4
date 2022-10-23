import flask

from env import THRESHOLD
from ai import vectorizer, model

NOT_OFFENSIVE_LABEL = "NOT_OFFENSIVE"
OFFENSIVE_LABEL = "OFFENSIVE"


app = flask.Flask(__name__)


@app.get("/")
def service():
    comment = flask.request.args["comment"]
    result = model.predict_proba(vectorizer.transform([comment]))
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
