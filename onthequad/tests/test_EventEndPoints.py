from __future__ import print_function
from falcon import testing
import pytest
import falcon
from onthequad.onthequad.app import api
from mock import patch


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


@pytest.fixture()
def client():
    return testing.TestClient(api)


@patch('onthequad.onthequad.dummyevents.DataBaseCalls.getAllEvents', return_value=doc)
# @patch.object(DataBaseCalls, 'getAllEvents', return_value="Butts")
def test_eventOnGet(mockGet, client):

    # mockGet.return_value = doc
    result = client.simulate_get('/dummyevents/')
    assert result.status == falcon.HTTP_OK
    assert mockGet() == result.json
