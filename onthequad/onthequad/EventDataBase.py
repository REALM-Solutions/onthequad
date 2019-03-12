import json
from .DataBaseSetUp import DataBaseSetUp
import time
database = DataBaseSetUp.setup()


class EventDatabase:


    def storeEvent(jsonObj):
        eid = database.child("Events").push(jsonObj)
        return eid['name']

    def getAllEvents():
        allEvents = database.child("Events").get()
        return allEvents.val()

    def updateEvent(eventId, updatedEvent):
        updated = database.child("Events").child(eventId).update(updatedEvent)
        return updated

    def deleteEvent(eventId):
        database.child("Events").child(eventId).remove()

    def getEventById(eventId):
        event = database.child("Events").child(eventId).get()
        return event.val()

    def getEventByName(name):
        event = database.child("Events").order_by_child("name").equal_to(name).get()
        return event.val()

    def getEventByCategory(category):
        events = database.child("Events").order_by_child("category").equal_to(category).get()
        return events.val()


    # # need to resturcture database to be flat.
    # def getEventByCreator(creator):
    #     events = database.child("Events").get()

    def getFutureEvents():
        events = database.child("Events").order_by_child("date").start_at(time.strftime("%m/%d/%Y")).get()
        return events.val()

    def getTest():
        event = database.child("Events").order_by_child("creator").order_by_child("username").equal_to("jpauga").get()
        return event.val()
