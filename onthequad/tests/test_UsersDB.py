from __future__ import print_function
from falcon import testing
import pytest
from onthequad.onthequad.UsersDB import database
from onthequad.onthequad.UsersDB import UsersDB
from onthequad.onthequad.DataBaseSetUp import DataBaseSetUp
from mock import patch, Mock
import mock

obj = {
    "firstName": "John",
    "lastName": "Smith",
    "email": "jsmith@msudenver.edu",
    "password": "jsmith",
    "photoURL": "",
    "events": []
}

objUpdated = {
        "id": 12345,
        "firstname": "John",
        "lastname": "Smith",
        "email": "jsmith@msudenver.edu",
        "username": "jsmith",
        "photoURL": "",
        "events": []
    }
    
@patch('onthequad.onthequad.UsersDB.database.get')
def test_getAllUsers(mockGet):
    UsersDB.getAllUsers()
    mockGet().assert_called


@patch('onthequad.onthequad.UsersDb.database.push')
def test_createUser(mockPush, uId):
    result = UsersDB.createUser(obj, uId)
    assert mockPush()["name"] == result
