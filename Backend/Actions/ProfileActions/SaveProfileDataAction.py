from Database import FireStore, Increment
from Model.Profile import Profile

def saveProfile(data):
    collectionName = 'Profiles'

    db = FireStore.getConnection()

    collection = db.collection(collectionName)

    latestDocContentID = Increment.getLatestDocument(db, collectionName)

    id = str(latestDocContentID+1)

    #create Model to reinforce layout of the object in the database:
    profile = Profile(id, data["Name"], data["FriendIDs"], data["ChatRoomIDs"])

    res = collection.document().set( #inserting document
        profile.toDict()
    )
    
    FireStore.closeConnection()
