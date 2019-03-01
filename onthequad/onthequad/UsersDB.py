import json
import pyrebase

config = {
'apiKey': "AIzaSyBEaQNRbDl0qmfTBORJ-4gbMdiBaSm3Q_o",
    'authDomain': "on-the-quad.firebaseapp.com",
    'databaseURL': "https://on-the-quad.firebaseio.com",
    'projectId': "on-the-quad",
    'storageBucket': "on-the-quad.appspot.com",
    'messagingSenderId': "535666577502"
}
firebase = pyrebase.initialize_app(config)
database = firebase.database()

class UserDataBase:

    def addUser(self, aUser):
        database.child("Users").push(aUser)

    def getUser(self, userId):
        user = database.child("Users").child(userId).get()
        return user.val()

    def getUsers(self):
        user = database.child("Users").get()
        return user.val()

    def updateUser(self, userId, updateUser):
        database.child("Users").child(userId).update(updateUser)

    def deleteUser(self, userId):
        database.child("Users").child(userId).remove()

    