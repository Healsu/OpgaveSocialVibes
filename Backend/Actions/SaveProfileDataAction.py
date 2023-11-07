from Database import FireStore, Increment
from firebase_admin import firestore
import datetime





def saveProfile(data):
    db = FireStore.getConnection()
    collection = db.collection('Profiles')
    latestDocID = Increment.getLatestDocument(db, 'Profiles')
    stringLatestDocID = str(latestDocID+1)
    print(stringLatestDocID)


    res = collection.document(stringLatestDocID).set({ #inserting document
    'ID': stringLatestDocID,
    'Name': data['Name'],
    'FriendIDs': data['FriendIDs'],
    'ChatRoomIDs': data['ChatRoomIDs'],
    'TimeStamp' : datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    })
    print(res)
    FireStore.closeConnection()


