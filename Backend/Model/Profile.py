import datetime

class Profile:
    def __init__(self, name):
        self.name = name
        self.timeTable = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    
    def toDict(self):
        data = {
            'Name': self.name,
            'TimeStamp': self.timeTable
        }
        
        return data
