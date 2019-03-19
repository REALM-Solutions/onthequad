from __future__ import print_function
from falcon import testing
import pytest
#from onthequad.onthequad.EventDataBase import database
from onthequad.onthequad.EventDataBase import EventDatabase
#from onthequad.onthequad.DataBaseSetUp import DataBaseSetUp
from mock import patch, Mock
import mock

obj = {
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
objUpdated = {
    "id": "123456",
    "name": "Studying",
    "location": "Study place",
    "date": "02/14/2019",
    "starttime": 1315,
    "endtime": 1430,
    "category": "Study",
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
objId = "123456"


@patch('onthequad.onthequad.EventDataBase.database.get')
def test_getAllEvents(mockGet):
    EventDatabase.getAllEvents()
    mockGet().assert_called


@patch('onthequad.onthequad.EventDataBase.database.push', return_value={"name":"123456"})
def test_storeEvent(mockPush):
    result = EventDatabase.storeEvent(obj)
    assert mockPush()["name"] == result


@patch('onthequad.onthequad.EventDataBase.database.remove', return_value=None)
def test_deleteEvent(mockDelete):
    result = EventDatabase.deleteEvent(objId)
    assert mockDelete() == result


@patch('onthequad.onthequad.EventDataBase.database.update')
def test_updateEvent(mockUpdate):
    EventDatabase.updateEvent(objId, obj)
    mockUpdate().assert_called


