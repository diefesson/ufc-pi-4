from flask import Flask, jsonify, abort, make_response, request
import pickle

VECTORIZER_PATH = "models/tf_idf_vectorizer.pickle"
MODEL_PATH = "models/tf_idf_svm_model.pickle"

NOT_OFFENSIVE_LABEL = "NOT_OFFENSIVE"
OFFENSIVE_LABEL = "OFFENSIVE"
LIMIT = 0.5

app = Flask(__name__)

with open(VECTORIZER_PATH, "br") as vectorizer_file, open(
    MODEL_PATH, "br"
) as model_file:
    vectorizer = pickle.load(vectorizer_file)
    model = pickle.load(model_file)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/comment-classifier/api/v1.0/analyze', methods=['GET'])
def comment_analyze():
     if not request.json or not 'body' in request.json:
        return abort(400)

     comment =  request.json.get('body', '')
     result = model.predict_proba(vectorizer.transform([comment]))

     not_offensive_prob, offensive_prob = result[0]
    
     classification = (
        OFFENSIVE_LABEL if offensive_prob > LIMIT else NOT_OFFENSIVE_LABEL
        )
     
     response = {
        "not_offensive_prob": not_offensive_prob,
        "offensive_prob": offensive_prob,
        "classification": classification,
     }

     return jsonify({'result': response})

if __name__ == '__main__':
    app.run(debug=True)