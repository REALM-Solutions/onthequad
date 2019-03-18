import falcon
from .EventEndPoints import EventEndPoints
from .dummyusers import DumUsers
from .UserEndPoints import UserEndPoints
from falcon_cors import CORS

cors = CORS(allow_origins_list=['http://localhost:8080'],
            allow_all_headers=True,
            allow_all_methods=True)

api = application = falcon.API(cors.middleware)

api.add_route('/events', EventEndPoints())
api.add_route('/dummyusers', DumUsers())
api.add_route('/UserEndPoints', UserEndPoints())
