import falcon
import json
from .DataBaseCalls import DataBaseCalls


class DumbEvents:

    def on_get(self, req, resp):
        # data = json.loads(req.stream.read())
        send = DataBaseCalls.getAllEvents()
        resp.body = json.dumps(send)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        # this logic can be removed since front end will input validation
        if any(data):
            send = {
                'Message' : 'Event has been created'
            }
            DataBaseCalls.storeEvent(data)
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_200
        else:
            send = {
                'Message' : 'Cannot create empty event'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_404

    def on_delete(self, req, resp):
        data = json.loads(req.stream.read())
        eventID = next(iter(data))
        if eventID is None:
            send = {
                'Message' : 'Event cannot be found'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_404
        else:
            send = {
                'Message' : "Event has been deleted"
            }
            DataBaseCalls.deleteEvent(eventID)
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        data = json.loads(req.stream.read())
        eventID = next(iter(data))
        if eventID is None:
            send = {
                'Message' : 'ID for event cannot be found'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_404
        else:
            DataBaseCalls.updateEvent(eventID, data[eventID])
            send = {
                'Message' : 'Event has been updated'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_200
