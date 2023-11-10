from Database import FireStore, Querys

def saveFriend(user_id, friend_id):
    db = FireStore.getConnection()
    #Get User Data and docs id
    userProfile, userDocsId = Querys.getById(db, "Profiles", user_id)
    friendProfile, friendDocsId = Querys.getById(db, "Profiles", friend_id)

    #append id to profile friends
    userProfile["FriendIds"].append(friend_id)
    friendProfile["FriendIds"].append(user_id)

    #send new profile back to the backend
    collection = db.collection('Profiles')
    collection.document(userDocsId).set( #inserting document
        userProfile
    )
    collection.document(friendDocsId).set( #inserting document
        friendProfile
    )
    FireStore.closeConnection()