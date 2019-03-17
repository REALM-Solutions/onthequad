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
    "email": "jsmith@msudenver.edu",
    "password": "jsmith",
}
updatedData = {
    "firstname": "UpdateJohn"
}

@pytest.fixture()
def client():
    return testing.TestClient(api)


@patch('onthequad.onthequad.UserEndPoints.UsersDB.getAllUsers', return_value=getData)
def test_successGet(mockGet, client):

    result = client.simulate_get('/users/')
    assert result.status == falcon.HTTP_OK
    assert mockGet() == result.json

# @patch('onthequad.onthequad.UserEndPoints.UsersDB.createUser', return_value=None)
# @patch('onthequad.onthequad.UserEndPoints.authen.create_user_with_email_and_password', return_value="1234")
# def test_successPost(mockPost, client):

#     result = client.simulate_post('/users', json=postData)
#     print(result.status)
#     assert falcon.HTTP_201 == result
    
#     assert {'message' : 'Account is successfully created'} == result.json


def test_failPost(client):

    result = client.simulate_post('/users', json={})
    assert falcon.HTTP_400 == result.status
    assert {'message' : 'Missing information. Try again'} == result.json


def test_successDelete(client):

    result = client.simulate_delete('/users', json={'123': {}})
    assert falcon.HTTP_OK == result.status
    assert {'message' : "User is successfully deleted"} == result.json


# def test_failDelete(client):

#     result = client.simulate_delete('/users', json={})
#     assert falcon.HTTP_400 == result.status
#     assert {'message' : 'User cannot be found'} == result.json


@patch('onthequad.onthequad.UserEndPoints.UsersDB.updateUser', return_value=updatedData)
def test_successPut(mockPut, client):

    result = client.simulate_put('/users', json={"user":"updated"})
    assert falcon.HTTP_OK == result.status
    #assert mockPut() == result.json
    assert {'message' : 'User is successfully updated'} == result.json


# def test_failPut(client):
#     result = client.simulate_put('/users', json={})
#     assert falcon.HTTP_400 == result.status
#     assert {'message' : 'Error. User not found'} == result.json