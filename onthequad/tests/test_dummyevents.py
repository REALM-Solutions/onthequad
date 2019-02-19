from falcon import testing
import pytest
import falcon
from onthequad.onthequad.app import api
import json


@pytest.fixture()
def client():
    # return testing.TestClient(api)
    return testing.TestClient(api)

# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_event_on_get(client):
    doc = {
        "id": 987654,
        "name": "Volleyball",
        "location": "Volleyball court",
        "date": "02/14/2019",
        "starttime": 1315,
        "endtime": 1430,
        "category": "Sports and Games",
        "creator": {
            "id": 12345,
            "firstname": "John",
            "lastname": "Smith",
            "email": "jsmith@msudenver.edu",
            "username": "jsmith",
            "photoURL": "",
            "events": []
        },
        "attendees": [],
        "availablespots": 10,
        "coordinates": "",
        "public": True
    }

    result = client.simulate_get('/dummyevents/')
    # result_doc = json.dumps(response)
    assert result.json == doc
    assert result.status == falcon.HTTP_OK


