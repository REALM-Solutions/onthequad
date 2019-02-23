import falcon
import json
from .EventDB import DataBaseCalls

class DumbEvents:

    def on_get(self, req, resp):
        # data = json.loads(req.stream.read())
        send = DataBaseCalls.getAllEvents()
        resp.body = json.dumps(send)
        resp.status = falcon.HTTP_200

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

        send = DataBaseCalls.updateEvent("-LZOf2FzoAad8_GPG5x7", data)
        # if data['method'] is None:
        #     sendback = {
        #         'msg': "there is nothing to update"
        #     }
        #     resp.body = json.dumps(sendback)
        #     resp.status = falcon.HTTP_400
        # else:
        #     sendback = {
        #         'msg': "Stuff will be updated"
        #     }
        resp.body = json.dumps(send)
        resp.status = falcon.HTTP_200
