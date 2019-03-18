import json
from .DataBaseSetUp import DataBaseSetUp

database = DataBaseSetUp.setup()

class UsersDB:

    def createUser(data, uId):
        database.child("Users").child(uId).set(data)

    def getAllUsers():
        allUsers = database.child("Users").get()
        return allUsers.val()

    def updateUser(userId, updatedUser):
        database.child("Users").child(userId).update(updatedUser)

    def deleteUser(userId):
        database.child("Users").child(userId).remove()

    def getUserById(userId):
        user = database.child(userId).get()
        return user.val()

    def getUserByEmail(email):
        user = database.child(email).get()
        return user.val()
        