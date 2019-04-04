import falcon
import json
from .User import User
from .UsersDB import UsersDB
from .DataBaseSetUp import DataBaseSetUp
authen = DataBaseSetUp.authentication()

class SignInEndPoints:

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        
        email = data['email']
        password = data['password']
        try:
            user = authen.sign_in_with_email_and_password(email, password)
            message = "log in successful"
            resp.body = json.dumps(message)
            resp.status = falcon.HTTP_200

        except:
            message = "invalid cerediantials"
            resp.body = json.dumps(message)
            resp.status = falcon.HTTP_400

        
