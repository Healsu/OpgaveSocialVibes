import datetime


class Message:
    def __init__(self, message, senderID, image_url=None):
        self.message = message
        self.image_url = image_url
        self.senderId = senderID
        self.isSeen = False
        self.timeStamp = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
        self.reactions = []

    def toDict(self):
        data = {
            'Message': self.message,
            'ImageURL': self.image_url,
            'SenderId': self.senderId,
            'isSeen': self.isSeen,
            'TimeStamp': self.timeStamp,
            'Reactions': self.reactions
        }

        return data
