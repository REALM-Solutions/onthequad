import falcon
from .EventEndPoints import EventEndPoints
from .dummyusers import DumUsers

api = application = falcon.API()

api.add_route('/events', EventEndPoints())
api.add_route('/dummyusers', DumUsers())
