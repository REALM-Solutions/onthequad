import json
from .DataBaseSetUp import DataBaseSetUp

database = DataBaseSetUp.setup()

class UsersDB:

    def createUser(data, uId):
        database.child("Users").child(uId).set(data.__dict__)#.__dict__

    def getAllUsers():
        allUsers = database.child("Users").get()
        return allUsers.val()

    def updateUser(userId, updatedUser):
        database.child("Users").child(userId).update(updatedUser)

    def deleteUser(userId):
        database.child("Users").child(userId).remove()

    def getUserById(userId):
        user = database.child('Users').child(userId).get()
        return user.val()
        
    
        