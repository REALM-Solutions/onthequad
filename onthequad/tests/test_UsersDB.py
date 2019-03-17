from __future__ import print_function
from falcon import testing
import pytest
#from onthequad.onthequad.UsersDB import database
from onthequad.onthequad.UsersDB import UsersDB
#from onthequad.onthequad.DataBaseSetUp import DataBaseSetUp
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
        "firstname": "UpdateJohn",
        "lastname": "Smith",
        "email": "jsmith@msudenver.edu",
        "username": "jsmith",
        "photoURL": "",
        "events": []
}

objId = "123456789"
  
@patch('onthequad.onthequad.UsersDB.database.get')
def test_getAllUsers(mockGet):
    UsersDB.getAllUsers()
    mockGet().assert_called


@patch('onthequad.onthequad.UsersDB.database.set')
def test_createUser(mockPush):
    result = UsersDB.createUser(obj, objId)
    #assert mockPush()["name"] == result

@patch('onthequad.onthequad.UsersDB.database.remove', return_value=None)
def test_deleteEvent(mockDelete):
    result = UsersDB.deleteUser(objId)
    assert mockDelete() == result


@patch('onthequad.onthequad.UsersDB.database.update')
def test_updateEvent(mockUpdate):
    UsersDB.updateUser(objId, obj)
    mockUpdate().assert_called