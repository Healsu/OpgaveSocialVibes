import datetime


class Event:
    def __init__(self, lat, lng, admin, title, description):
        self.title = title
        self.admin = admin
        self.lat = lat
        self.lng = lng
        self.description = description
        self.timeTable = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")

    def toDict(self):
        data = {
            'Title': self.title,
            'Description': self.description,
            'Latitude': self.lat,
            'Longitude': self.lng,
            'Admin': self.admin,
            'TimeStamp': self.timeTable
        }
            
        return data
