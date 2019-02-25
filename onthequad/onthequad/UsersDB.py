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

    def pushUser(jsonObj):
        database.child("Users").push(jsonObj)

    def getUser(userId):
        allEvents = database.child("Users").child(userId).get()
        return allEvents.val()

    def postUser(userId, updateUser):
        database.child("Users").child(userId).update(updateUser)

    def deleteUser(userId):
        database.child("Users").child(userId).remove()

    