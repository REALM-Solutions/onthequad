import falcon
from .EventEndPoints import EventEndPoints
from .dummyusers import DumUsers
from .UserEndPoints import UserEndPoints
import requests

ALLOWED_ORIGINS = ["http://localhost:8000"]

class CorsMiddleware(object):

    def process_request(self, request, response):
        origin = request.get_header('Origin')
        if origin in ALLOWED_ORIGINS:
            response.set_header('Access-Control-Allow-Origin', origin)

api = application = falcon.API(middleware=[CorsMiddleware()])

api.add_route('/events', EventEndPoints())
api.add_route('/dummyusers', DumUsers())
api.add_route('/UserEndPoints', UserEndPoints())
