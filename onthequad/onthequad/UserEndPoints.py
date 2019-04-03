import falcon
import json
from .User import User
from .UsersDB import UsersDB
from .DataBaseSetUp import DataBaseSetUp
authen = DataBaseSetUp.authentication()

class UserEndPoints:

    def on_get(self, req, resp):
        params = req.params
        if 'id' in params:
            send = {
                params['id']:
                UsersDB.getUserById(params['id'])
            }

        else:
            send = UsersDB.getAllUsers()
        resp.body = json.dumps(send)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())

        if any(data):

            try:

                email = data['email']
                password = data['password']
                firstName = data['firstName']
                lastName = data['lastName']
                photoUrl = data['photoUrl']

            except:
                send = {"msg": "missing fields"}
                resp.body = json.dumps(send)
                resp.status = falcon.HTTP_400
                return

            #Create userName
            emailArray = email.split("@")
            userName = emailArray[0]

            #Create user authentication
            user = authen.create_user_with_email_and_password(email, password)
            uId = user['localId']

            #Put user info into Database
            userObject = User(uId, firstName, lastName, email, userName, photoUrl)
            aUser = UsersDB.createUser(userObject, uId)

            sendBack = {

                    aUser : userObject.__dict__
            }

            resp.body = json.dumps(sendBack)
            resp.status = falcon.HTTP_201

        else:
            sendBack = {
                'message' : 'Cannot create an empty user.'
            }
            resp.body = json.dumps(sendBack)
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
