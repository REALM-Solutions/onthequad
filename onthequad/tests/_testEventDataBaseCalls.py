# import pytest
# from mock import Mock, patch
# from onthequad.onthequad.DataBaseCalls import DataBaseCalls
#
# @pytest.fixture(scope='module')
# def eventDataBase(request):
#     mockDataBase = {
#        "events": {
#           {
#              "id": 987654,
#              "name": "Volleyball",
#              "location": "Volleyball court",
#              "date": "02/14/2019",
#              "starttime": 1315,
#              "endtime": 1430,
#              "category": "Sports",
#              "creator": {
#                 "id": 12345,
#                 "firstname": "John",
#                 "lastname": "Smith",
#                 "email": "jsmith@msudenver.edu",
#                 "username": "jsmith",
#                 "photoURL": "",
#                 "events": []
#              },
#              "attendees": [],
#              "availablespots": 10,
#              "coordinates": "",
#              "public": True
#           },
#           {
#              "id": 987655,
#              "name": "SweetHeart Dance",
#              "location": "Gymnasium",
#              "date": "02/14/2019",
#              "starttime": 1315,
#              "endtime": 1430,
#              "category": "Causal",
#              "creator": {
#                 "id": 12345,
#                 "firstname": "John",
#                 "lastname": "Smith",
#                 "email": "jsmith@msudenver.edu",
#                 "username": "jsmith",
#                 "photoURL": "",
#                 "events": []
#              },
#              "attendees": [],
#              "availablespots": 10,
#              "coordinates": "",
#              "public": True
#           },
#           {
#              "id": 983727,
#              "name": "Chem Study",
#              "location": "Library",
#              "date": "03/19/19",
#              "startTime": 1100,
#              "endTime": 1300,
#              "category": "Study",
#              "creator": {
#                 "id": 12346,
#                 "firstname": "Justin",
#                 "lastname": "Pauga",
#                 "email": "jpauga@msudenver.edu",
#                 "username": "jpauga",
#                 "photoURL": "",
#                 "events": []
#              },
#              "attendees": [],
#              "availablespots": 6,
#              "coordinates": "",
#              "public": True
#           }
#        }
#     }
#     def fin():
#         print('\n[teardown] cheese_db finalizer, disconnect from db')
#     request.addfinalizer(fin)
#     return mockDataBase
#
# def _testGetEvent(eventDataBase):
#     print('in test for get')
