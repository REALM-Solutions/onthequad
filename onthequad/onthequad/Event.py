
class Events:
    def __init__(self, id, name, location, date, starttime, endtime, category, creator, attendees, availablespots,
                 coordinates, public):
        self.id = id
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
