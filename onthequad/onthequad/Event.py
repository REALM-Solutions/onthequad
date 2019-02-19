import uuid
class Events:
    def __init__(self, name, location, date, starttime, endtime, category, creator, attendees, availablespots,
                 coordinates, public):
        self.id = uuid.uuid1()
        self.name = name
        self.location = location
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.category = category
        self.creator = creator
        self.attendees = attendees
        self.availablespots = availablespots
        self.coordinates = coordinates
        self.public = public
