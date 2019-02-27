import pyrebase
import falcon
from .events import Event
from .dummyevents import DumbEvents
from .users import User
from .dummyusers import DumUsers

api = application = falcon.API()

api.add_route('/events', Event())
api.add_route('/dummyevents', DumbEvents())
api.add_route('/users', User())

api.add_route('/dummyusers', DumUsers())
