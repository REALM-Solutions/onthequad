import pyrebase
import falcon
from .events import Event
from .users import User
from .dummyusers import DumUsers

config = {
'apiKey': "AIzaSyBEaQNRbDl0qmfTBORJ-4gbMdiBaSm3Q_o",
    'authDomain': "on-the-quad.firebaseapp.com",
    'databaseURL': "https://on-the-quad.firebaseio.com",
    'projectId': "on-the-quad",
    'storageBucket': "on-the-quad.appspot.com",
    'messagingSenderId': "535666577502"
}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()

api = application = falcon.API()

api.add_route('/events', Event())

api.add_route('/dummyusers', DumUsers())
api.add_route('/users', User())


