import json
from .DataBaseSetUp import DataBaseSetUp

database = DataBaseSetUp.setup()

class UsersDB:

    def createUser(data):
        database.child("Users").push(data)

    def getAllUsers():
        allUsers = database.child("Users").get()
        return allUsers.val()

    def updateUser(userId, updatedUser):
        database.child("Users").child(userId).update(updatedUser)

    def deleteUser(userId):
        database.child("Users").child(userId).remove()