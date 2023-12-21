import datetime


class Event:
    def __init__(self, lat, lng, admin, title, description, start_date, stop_date, adress, start_time, stop_time):
        self.title = title
        self.admin = admin
        self.lat = lat
        self.lng = lng
        self.description = description
        self.start_date = start_date
        self.stop_date = stop_date
        self.start_time = start_time
        self.stop_time = stop_time
        self.adress = adress
        self.timeTable = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")

    def toDict(self):
        data = {
            'Title': self.title,
            'Description': self.description,
            'Latitude': self.lat,
            'Longitude': self.lng,
            'Adress': self.adress,
            'StartDate': self.start_date,
            'StartTime': self.start_time,
            'StopDate': self.stop_date,
            'StopTime': self.stop_time,
            'Admin': self.admin,
            'TimeStamp': self.timeTable
        }
            
        return data
