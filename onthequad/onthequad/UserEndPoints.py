import json, falcon
from .UsersDB import UserDataBase

class UserEndPoints:

    def createUser(self, req, resp):

        data = json.loads(req.stream.read())
        
        fname = data["body"].firstName
        lname = data["body"].lastName
        email = data["body"].email
        arrayEmail = email.split("@")
        userName = arrayEmail[0] 
        events = []
        aUser = {
            "firstName": fname
            "lastName": lname 
            "email": email
            "user":userName 
            "evetns": events = []
        }
        

    

