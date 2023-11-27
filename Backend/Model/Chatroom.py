import datetime


class Chatroom:
    def __init__(self, admin, title, LatestMessage):
        self.type = None
        self.title = title
        self.admin = admin
        self.LatestMessage = LatestMessage
        self.timeTable = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")

    def toDict(self):
        data = {
            'Title': self.title,
            'Admin': self.admin,
            'LatestMessage': self.LatestMessage,
            'TimeStamp': self.timeTable
        }

        if self.type is not None:
            data['Type'] = self.type
            
        return data
    
    def setType(self, count):
        self.type = 'Group Chat' if len(count) > 2 else 'Individual Chat'