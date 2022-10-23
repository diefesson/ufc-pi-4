import pytest
import requests
import multiprocessing
from time import sleep
from marshmallow import Schema, fields, validate

from env import HOST, PORT
from server import serve


ENDPOINT = f"http://{HOST}:{PORT}"


ok_response_schema: Schema = Schema.from_dict(
    {
        "not_offensive_prob": fields.Float(
            required=True,
        ),
        "offensive_prob": fields.Float(
            required=True,
        ),
        "classification": fields.String(
            required=True,
            validate=validate.OneOf(["OFFENSIVE", "NOT_OFFENSIVE"]),
        ),
    }
)()

fail_response_schema: Schema = Schema.from_dict(
    {
        "error": fields.String(
            required=True, validate=validate.OneOf(["INVALID_REQUEST"])
        ),
        "error_details": fields.Raw(required=True),
    }
)()


@pytest.fixture(autouse=True, scope="session")
def setup_server():
    """Setups server for endpoint testing"""
    server_process = multiprocessing.Process(target=serve, args=(HOST, PORT))
    server_process.start()
    # Awaits for server to start
    sleep(5)
    yield
    server_process.terminate()


def test_server_ok():
    """Tests if server return the a well formed response for a well formed request"""
    res = requests.get(
        ENDPOINT,
        params={
            "comment": "Tis but a scratch",
        },
    )
    status_code = res.status_code
    validation_errors = ok_response_schema.validate(res.json())
    assert status_code == 200
    print(validation_errors)
    assert len(validation_errors) == 0


def test_server_fail():
    """Tests if servers fails gracefully for a ill formed request"""
    res = requests.get(
        ENDPOINT,
        params={
            # Notice the mispelled key
            "commen": "The worst day of you life so far"
        },
    )
    status_code = res.status_code
    validation_errors = fail_response_schema.validate(res.json())
    print(res.json())
    assert status_code == 400
    assert len(validation_errors) == 0
