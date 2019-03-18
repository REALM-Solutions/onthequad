import falcon
import json
from .EventDataBase import EventDatabase


class EventEndPoints:


    def on_get(self, req, resp):
        data = json.loads(req.stream.read())
        params = req.params
        # print(params)
        if 'id' in params:
            send = {
                params['id']:
                EventDatabase.getEventById(params['id'])
            }
            # resp.body = json.dumps(send)
        elif 'name' in params:
            send = EventDatabase.getEventByName(params['name'])
        elif 'category' in params:
            send = EventDatabase.getEventByCategory(params['category'])
        elif 'creatorId' in params:
            send = EventDatabase.getEventByCreator(params['creatorId'])
        elif 'myevents' in params:
            send = EventDatabase.getMyEvents(params['myevents'])
        else:
            send = EventDatabase.getTest()
            resp.body = json.dumps(send)
        resp.body = json.dumps(send)
        resp.status = falcon.HTTP_200


    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        if any(data):
            params = req.params
            if 'userid' in params:

                eventId = EventDatabase.storeEvent(data, params['userid'])
                send = {
                    eventId : data

                }
                resp.body = json.dumps(send)
                resp.status = falcon.HTTP_201
            elif 'attending' in params:
                EventDatabase.updateAttending(params['attending'][0], params['attending'][1])
            else:
                send = {
                    'Message': 'Need userId'
                }
                resp.body = json.dumps(send)
                resp.status = falcon.HTTP_400
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
