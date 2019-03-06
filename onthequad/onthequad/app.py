import falcon
from .EventEndPoints import EventEndPoints
from .dummyusers import DumUsers
from .UserEndPoints import UserEndPoints

api = application = falcon.API()

api.add_route('/events', EventEndPoints())
api.add_route('/dummyusers', DumUsers())
api.add_route('/UserEndPoints', UserEndPoints())
