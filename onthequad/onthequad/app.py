import pyrebase
import falcon
from .events import Event
from .dummyevents import DumbEvents
from .UserEndPoints import UserEndPoints
from .dummyusers import DumUsers

api = application = falcon.API()

api.add_route('/events', Event())
api.add_route('/dummyevents', DumbEvents())
api.add_route('/UserEndPoints', UserEndPoints())
api.add_route('/dummyusers', DumUsers())
