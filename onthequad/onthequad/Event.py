
class Event:
    def __init__(self, name, location, date, startTime, endTime, category, creator, availableSpots, description,
                 coordinates, public):
        self.name = name
        self.location = location
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.category = category
        self.creator = creator
        self.description = description
        self.availableSpots = availableSpots
        self.coordinates = coordinates
        self.public = public
