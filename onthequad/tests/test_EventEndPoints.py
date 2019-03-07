from __future__ import print_function
from falcon import testing
import pytest
import falcon
from onthequad.onthequad.app import api
from mock import patch


getDoc = {
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
postDoc = {
    "event": "test"
}
updatedDoc = {
    "event": "updated"
}


@pytest.fixture()
def client():
    return testing.TestClient(api)


@patch('onthequad.onthequad.EventEndPoints.EventDatabase.getAllEvents', return_value=getDoc)
def test_successOnGet(mockGet, client):

    result = client.simulate_get('/events/')
    assert result.status == falcon.HTTP_OK
    assert mockGet() == result.json


@patch('onthequad.onthequad.EventEndPoints.EventDatabase.storeEvent', return_value='123')
def test_successOnPost(mockPost, client):

    result = client.simulate_post('/events', json=postDoc)
    assert falcon.HTTP_201 == result.status
    assert {'123':postDoc} == result.json


def test_failOnPost(client):

    result = client.simulate_post('/events', json={})
    assert falcon.HTTP_400 == result.status
    assert {"Message": "Cannot create empty event"} == result.json


def test_successOnDelete(client):

    result = client.simulate_delete('/events', json={'123': {}})
    assert falcon.HTTP_OK == result.status
    assert {'Message' : "Event has been deleted"} == result.json


def test_failOnDelete(client):

    result = client.simulate_delete('/events', json={})
    assert falcon.HTTP_400 == result.status
    assert {'Message' : "Event cannot be found"} == result.json


@patch('onthequad.onthequad.EventEndPoints.EventDatabase.updateEvent', return_value=updatedDoc)
def test_successOnPut(mockPut, client):

    result = client.simulate_put('/events', json={"event":"updated"})
    assert falcon.HTTP_OK == result.status
    assert mockPut() == result.json


def test_failOnPut(client):
    result = client.simulate_put('/events', json={})
    assert falcon.HTTP_400 == result.status
    assert {'Message' : 'ID for event cannot be found'} == result.json
