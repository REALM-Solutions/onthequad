import json
from .DataBaseSetUp import DataBaseSetUp

database = DataBaseSetUp.setup()


class EventDatabase:


    def storeEvent(jsonObj):
        database.child("Events").push(jsonObj)

    def getAllEvents():
        allEvents = database.child("Events").get()
        return allEvents.val()

    def updateEvent(eventID, updatedEvent):
        database.child("Events").child(eventID).update(updatedEvent)

    def deleteEvent(eventID):
        database.child("Events").child(eventID).remove()
