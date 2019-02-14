import falcon
from .events import Event
from .users import User

api = application = falcon.API

api.add_route('/events', Event())
api.add_route('/users', User())


