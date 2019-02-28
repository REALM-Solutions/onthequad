import json
from .DataBaseSetUp import DataBaseSetUp

database = DataBaseSetUp.setup()


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
