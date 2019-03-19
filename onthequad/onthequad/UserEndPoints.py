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
            email = data['email']
            password = data['password']
            firstname = data['firstName']
            lastName = data['lastName']
            photoUrl = data['photoUrl']
            
            emailArray = email.split("@")
            userName = emailArray[0]
            
            #userObject = User(email, password, )
            user = authen.create_user_with_email_and_password(email, password)
            uId = user['localId']
            
            aUser = {
                "email": email,
                "firstName": firstname,
                "lastName": lastName,
                "userName": userName,
                "photoUrl": photoUrl,
                "eventsAttending": [],
                "eventsCreated": []
            }

            UsersDB.createUser(aUser, uId)

            sendBack = {
                "message" : 'Account is successfully created',
                "useId": uId,
                "email": email,
                "firstName": firstname,
                "lastName": lastName,
                "userName": userName,
                "photoUrl": photoUrl,
                "eventsAttending": [],
                "eventsCreated": []
            }
            resp.body = json.dumps(sendBack)
            resp.status = falcon.HTTP_201
        else:
            sendBack = {
                'message' : 'Missing information. Try again'
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

            
        

    

