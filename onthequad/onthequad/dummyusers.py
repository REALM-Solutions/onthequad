import falcon
import json


class DumUsers:

    def on_get(self, req, resp):
        data = json.loads(req.stream.read())

        sendback = {
            "id": 12345,
            "firstName": "John",
            "lastName": "Smith",
            "email": "jsmith@msudenver.edu",
            "userName": "jsmith",
            "photoURL": "",
            "events": []
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
                'msg': "stuff will be delete"
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

            