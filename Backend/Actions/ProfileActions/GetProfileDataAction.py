from Database import FireStore, Querys
from Model.Profile import Profile

def getProfile(user_id):
    db = FireStore.getConnection()
    
    profile_data = Querys.getById(db, "Profiles", user_id)
    
    FireStore.closeConnection()
    return profile_data