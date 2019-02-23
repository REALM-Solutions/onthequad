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

authe = firebase.auth()
database = firebase.database()

class DataBaseCalls:


    def storeEvent(jsonObj):
        database.child("Event").push(jsonObj)

    def getAllEvents():
        allEvents = database.child("Event").get()
        return allEvents.val()

    def updateEvent(eventID, updatedEvent):
        database.child("Event").child(eventID).update(updatedEvent)

    def deleteEvent(eventID):
        database.child("Event").child(eventID).remove()
