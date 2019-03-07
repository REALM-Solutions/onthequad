import json
from .DataBaseSetUp import DataBaseSetUp

database = DataBaseSetUp.setup()


class EventDatabase:


    def storeEvent(jsonObj):
        eid = database.child("Events").push(jsonObj)
        return eid['name']

    def getAllEvents():
        allEvents = database.child("Events").get()
        return allEvents.val()

    def updateEvent(eventID, updatedEvent):
        updated = database.child("Events").child(eventID).update(updatedEvent)
        return updated

    def deleteEvent(eventID):
        database.child("Events").child(eventID).remove()
