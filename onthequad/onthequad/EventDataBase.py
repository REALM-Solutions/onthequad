import json
from .DataBaseSetUp import DataBaseSetUp
from datetime import datetime
database = DataBaseSetUp.setup()


class EventDatabase:


    def storeEvent(Obj, userId):
        eid = database.child("Events").push(Obj.__dict__)
        database.child("Host").child(userId).child(eid['name']).set("")
        return eid['name']


    def addAttending(userId, eventId):
        database.child("Attending").child(eventId).child(userId).set("")
        database.child("MyEvents").child(userId).child(eventId).set("")


    def removeAttending(userId, eventId):
        database.child("Attending").child(eventId).child(userId).remove()
        database.child("MyEvents").child(userId).child(eventId).remove()


    def getAllEvents():
        allEvents = database.child("Events").get().val()
        return allEvents


    def updateEvent(eventId, updatedEvent):
        updated = database.child("Events").child(eventId).update(updatedEvent)
        return updated


    def deleteEvent(eventId):
        database.child("Events").child(eventId).remove()
        userIds = database.child("Attending").child(eventId).shallow().get().val()
        if userIds is not None:
            for userId in userIds:
                database.child("MyEvents").child(userId).child(eventId).remove()
                database.child("Host").child(userId).child(eventId).remove()
            database.child("Attending").child(eventId).remove()
        hostIds = database.child("Host").shallow().get().val()
        for hostId in hostIds:
            database.child("Host").child(hostId).child(eventId).remove()

    def getEventById(eventId):
        event = database.child("Events").child(eventId).get().val()
        return event


    def getEventByName(name):
        event = database.child("Events").order_by_child("name").equal_to(name).get().val()
        return event


    def getEventByCategory(category):
        events = database.child("Events").order_by_child("category").equal_to(category).get().val()
        return events


    def getEventByCreator(hostId):
        eventIds = database.child("Host").child(hostId).shallow().get().val()
        eventObj = EventDatabase.getEventObject(eventIds)
        return eventObj


    def getFutureEvents():
        events = database.child("Events").order_by_child("date").start_at(str(datetime.now())).get().val()
        return events


    def getMyEvents(userId):
        eventIds = database.child("MyEvents").child(userId).shallow().get().val()
        eventObj = EventDatabase.getEventObject(eventIds)
        return eventObj

    def getTest(eventId):
        event = database.child("Host").shallow().get().val()

        print(event)


    def getEventObject(idList):
        eventObj = {}
        for eventId in idList:
            event = database.child("Events").child(eventId).get().val()
            data = {eventId: event}
            eventObj.update(data)
        return eventObj