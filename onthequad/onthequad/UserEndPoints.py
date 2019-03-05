import falcon
import json
from .UsersDB import UsersDB
from .DataBaseSetUp import DataBaseSetUp
authen = DataBaseSetUp.authentication()

class UserEndPoints:

    def on_get(self, req, resp):
        
        send = UsersDB.getAllUsers()
        resp.body = json.dumps(send)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
    
        if any(data):

            user = authen.create_user_with_email_and_password(data['email'], data['password'])
            del data['password']

            send = {
                'message' : 'Account is successfully created'
            }

            UsersDB.createUser(data)
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_201
        else:
            send = {
                'message' : 'Missing information. Try again'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_400

    def on_delete(self, req, resp):
        data = json.loads(req.stream.read())
        userId = next(iter(data))
        if userId is None:
            send = {
                'message' : 'User cannot be found'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_400
        else:
            send = {
                'message' : "User is successfully deleted"
            }
            UsersDB.deleteUser(userId)
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        data = json.loads(req.stream.read())
        userId = next(iter(data))
        if userId is None:
            send = {
                'message' : 'Error. User not found'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_400
        else:
            UsersDB.updateUser(userId, data[userId])
            send = {
                'message' : 'User is successfully updated'
            }
            resp.body = json.dumps(send)
            resp.status = falcon.HTTP_200

            
        

    

