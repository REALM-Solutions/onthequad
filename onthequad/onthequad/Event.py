
class Event:
    def __init__(self, name, location, date, startTime, endTime, category, creator, availableSpots,
                 coordinates, public):
        self.name = name
        self.location = location
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.category = category
        self.creator = creator
        self.availableSpots = availableSpots
        self.coordinates = coordinates
        self.public = public
