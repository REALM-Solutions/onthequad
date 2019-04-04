import falcon
import json
from .EventDataBase import EventDatabase


class EventEndPoints:


    def on_get(self, req, resp):
        send = EventDatabase.getAllEvents()
        resp.body = json.dumps(send)
        resp.status = falcon.HTTP_200


    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        # this logic can be removed since front end will input validation
        if any(data):

            eventId = EventDatabase.storeEvent(data)
            send = {
                eventId : data

            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_201
        else:
            send = {
                'Message' : 'Cannot create empty event'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_400

    def on_delete(self, req, resp):
        data = json.loads(req.stream.read())

        if any(data):
            send = {
                'Message' : "Event has been deleted"
            }
            eventID = next(iter(data))
            EventDatabase.deleteEvent(eventID)
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_200
        else:
            send = {
                'Message' : 'Event cannot be found'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_400

    def on_put(self, req, resp):
        data = json.loads(req.stream.read())

        if any(data):
            eventID = next(iter(data))
            send = EventDatabase.updateEvent(eventID, data[eventID])

            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_200
        else:

            send = {
                'Message' : 'ID for event cannot be found'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_400
