import datetime

class Profile:
    def __init__(self, id, name, friendIds, chatRoomIds):
        self.id = id
        self.name = name
        self.friendIds = friendIds
        self.chatRoomIds = chatRoomIds
        self.timeTable = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    
    def toDict(self):
        return {
           'ID': self.id,
           'Name': self.name,
           'FriendIds': self.friendIds,
           'ChatRoomIds': self.chatRoomIds,
           'TimeStamp': self.timeTable
       }