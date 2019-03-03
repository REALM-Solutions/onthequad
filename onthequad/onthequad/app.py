import falcon
from .EventEndPoints import EventEndPoints
from .users import User
from .dummyusers import DumUsers

api = application = falcon.API()

api.add_route('/events', EventEndPoints())
api.add_route('/users', User())

api.add_route('/dummyusers', DumUsers())
