from __future__ import print_function
from falcon import testing
import pytest
import falcon
from onthequad.onthequad.app import api
from mock import patch


getData = {
        "firstname": "John",
        "lastname": "Smith",
        "email": "jsmith@msudenver.edu",
        "username": "jsmith",
        "photoURL": "",
        "events": []
}
postData = {
    "user": "test"
}
updatedData = {
    "user": "updatedUser"
}

@pytest.fixture()
def client():
    return testing.TestClient(api)

@patch('onthequad.onthequad.UserEndPoints.UsersDB.getAllUsers', return_value=getData)
def test_successGet(mockGet, client):

    result = client.simulate_get('/users/')
    assert result.status == falcon.HTTP_OK
    assert mockGet() == result.json

@patch('onthequad.onthequad.UserEndPoints.UsersDB.createUser', return_value=None)
def test_successPost(mockPost, client):

    result = client.simulate_post('/users', json=postData)
    assert falcon.HTTP_201 == result.status
    assert {'123':postData} == result.json


def test_failPost(client):

    result = client.simulate_post('/users', json={})
    assert falcon.HTTP_400 == result.status
    assert {"Message": "Cannot create empty user"} == result.json


def test_successDelete(client):

    result = client.simulate_delete('/users', json={'123': {}})
    assert falcon.HTTP_OK == result.status
    assert {'Message' : "User has been deleted"} == result.json


def test_failDelete(client):

    result = client.simulate_delete('/users', json={})
    assert falcon.HTTP_400 == result.status
    assert {'Message' : "User cannot be found"} == result.json


@patch('onthequad.onthequad.UserEndPoints.UsersDB.updateUser', return_value=updatedDoc)
def test_successPut(mockPut, client):

    result = client.simulate_put('/users', json={"user":"updated"})
    assert falcon.HTTP_OK == result.status
    assert mockPut() == result.json


def test_failPut(client):
    result = client.simulate_put('/users', json={})
    assert falcon.HTTP_400 == result.status
    assert {'Message' : 'ID for user cannot be found'} == result.json