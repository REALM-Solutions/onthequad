import falcon
from .EventEndPoints import EventEndPoints
from .UserEndPoints import UserEndPoints
from .UserSignInEndPoints import UserSignInEndPoints
from falcon_cors import CORS

cors = CORS(allow_all_origins=['http://localhost:3000'],
            allow_all_headers=True,
            allow_all_methods=True)

api = application = falcon.API(middleware=[cors.middleware])

api.add_route('/events', EventEndPoints())
api.add_route('/users', UserEndPoints())
api.add_route('/signin', UserSignInEndPoints())
