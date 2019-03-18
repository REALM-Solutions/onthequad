import json
from .DataBaseSetUp import DataBaseSetUp
from datetime import datetime
database = DataBaseSetUp.setup()


class EventDatabase:


    def storeEvent(jsonObj, userId):
        eid = database.child("Events").push(jsonObj)
        database.child("CreatedBy").child(userId).child(eid['name']).set("")
        return eid['name']


    def updateAttending(userId, eventId):
        database.child("Attending").child(eventId).child(userId).set("")


    def getAllEvents():
        allEvents = database.child("Events").get().val()
        return allEvents


    def updateEvent(eventId, updatedEvent):
        updated = database.child("Events").child(eventId).update(updatedEvent)
        return updated


    def deleteEvent(eventId):
        database.child("Events").child(eventId).remove()


    def getEventById(eventId):
        event = database.child("Events").child(eventId).get().val()
        return event


    def getEventByName(name):
        event = database.child("Events").order_by_child("name").equal_to(name).get().val()
        return event


    def getEventByCategory(category):
        events = database.child("Events").order_by_child("category").equal_to(category).get().val()
        return events


    def getEventByCreator(creatorId):
        events = database.child("CreatedBy").child(creatorId).shallow().get().val()
        eventObj = {}
        for eventId in events:
            event = database.child("Events").child(eventId).get().val()
            data = {eventId: json.dumps(event)}
            eventObj.update(data)
        print(eventObj)


    def getFutureEvents():
        events = database.child("Events").order_by_child("date").start_at(str(datetime.now())).get().val()
        return events


    def getMyEvents(userId):
        events = database.child("Attending").order_by_key().order_by_child(userId).get().val()
        print(events)


    def getTest():
        event = database.child("Events").order_by_child("date").start_at(str(datetime.now())).get().val()
        print(event)
        # return event
