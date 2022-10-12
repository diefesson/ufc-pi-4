import pickle as pk
import flask

VECTORIZER_PATH = "models/tf_idf_vectorizer.pickle"
MODEL_PATH = "models/tf_idf_svm_model.pickle"

THRESHOLD = 0.5
NOT_OFFENSIVE_LABEL = "NOT_OFFENSIVE"
OFFENSIVE_LABEL = "OFFENSIVE"


with open(VECTORIZER_PATH, "br") as vectorizer_file, open(
    MODEL_PATH, "br"
) as model_file:
    vectorizer = pk.load(vectorizer_file)
    model = pk.load(model_file)

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


app.run(port=4000)
