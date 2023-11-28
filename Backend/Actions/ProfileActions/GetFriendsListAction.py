from Database import FireBaseDatabase, Querys
from Model.Profile import Profile

def getFriends(user_id):


    db = FireBaseDatabase.getConnection()
    #get the profle
    profile_data = Querys.getById(db, "Profiles", user_id)
    #get the friends list
    friends = profile_data['FriendIds']

    friend_list = []

    if(len(friends)==0): #guard aginst faults
        return []

    #iterate and get the friends objects from the friends list
    for friend in friends:
        friend_data = Querys.getById(db, "Profiles", friend)
        friend_list.append(friend_data)
    
    FireBaseDatabase.closeConnection()

    return friend_list