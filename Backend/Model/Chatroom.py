import datetime


class Chatroom:
    def __init__(self, id, participantsIds, adminId):
        self.id = id
        self.participantsIds = participantsIds
        self.type = 'Group Chat' if len(participantsIds) > 2 else 'Individual Chat'
        self.adminId = adminId
        self.ChatMessageIds = []
        self.LatestMessage = None
        self.timeTable = datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")

    def toDict(self):
        return {
            'ID': self.id,
            'Type': self.type,
            'ParticipantsId': self.participantsIds,
            'AdminID': self.adminId,
            'ChatMessageIds': self.ChatMessageIds,
            'LatestMessage': self.LatestMessage,
            'TimeStamp': self.timeTable
        }