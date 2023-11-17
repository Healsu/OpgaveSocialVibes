import datetime


class Message:
    def __init__(self, message, senderID):
        self.message = message
        self.senderId = senderID
        self.isSeen = False
        self.timeStamp = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
        self.reactions = []

    def toDict(self):
        data = {
            'Message': self.message,
            'SenderId': self.senderId,
            'isSeen': self.isSeen,
            'TimeStamp': self.timeStamp,
            'Reactions': self.reactions
        }

        return data
