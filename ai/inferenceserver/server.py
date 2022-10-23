import flask
from marshmallow import Schema, fields, ValidationError

from env import THRESHOLD
from ai import vectorizer, model

NOT_OFFENSIVE_LABEL = "NOT_OFFENSIVE"
OFFENSIVE_LABEL = "OFFENSIVE"


request_params_schema: Schema = Schema.from_dict(
    {
        "comment": fields.String(required=True),
    }
)()


def infer(comment):
    features = vectorizer.transform([comment])
    result = model.predict_proba(features)
    not_offensive_prob, offensive_prob = result[0]
    classification = (
        OFFENSIVE_LABEL if offensive_prob > THRESHOLD else NOT_OFFENSIVE_LABEL
    )
    return not_offensive_prob, offensive_prob, classification


def make_error_response(error_code, error_messages):
    return {
        "error_code": error_code,
        "error_messages:": error_messages,
    }, 400


app = flask.Flask(__name__)


@app.get("/")
def service():
    try:
        args = request_params_schema.load(flask.request.args)
        comment = args["comment"]
    except ValidationError as e:
        return make_error_response("INVALID_REQUEST", e.messages)
    offensive_prob, not_offensive_prob, classification = infer(comment)
    return {
        "not_offensive_prob": not_offensive_prob,
        "offensive_prob": offensive_prob,
        "classification": classification,
    }


def serve(host, port):
    app.run(host=host, port=port)
