import falcon
import json


class DumbEvents:

    def on_get(self, req, resp):
        data = json.loads(req.stream.read())

        sendback = {
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

        resp.body = json.dumps(sendback)

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        if data['method'] == 'OK':
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404

    def on_delete(self, req, resp):
        data = json.loads(req.stream.read())

        if data['method'] is None:
            sendback = {
                'msg': "there is nothing to delete"
            }
            resp.body = json.dumps(sendback)
            resp.status = falcon.HTTP_400
        else:
            sendback = {
                'msg': "stuff will be delted"
            }
            resp.body = json.dumps(sendback)
            resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        data = json.loads(req.stream.read())

        if data['method'] is None:
            sendback = {
                'msg': "there is nothing to update"
            }
            resp.body = json.dumps(sendback)
            resp.status = falcon.HTTP_400
        else:
            sendback = {
                'msg': "Stuff will be updated"
            }
            resp.body = json.dumps(sendback)
            resp.status = falcon.HTTP_200
