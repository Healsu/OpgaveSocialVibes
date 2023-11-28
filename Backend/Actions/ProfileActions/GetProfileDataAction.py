from Database import FireBaseDatabase, Querys
from Model.Profile import Profile

def getProfile(user_id):
    db = FireBaseDatabase.getConnection()
    
    profile_data = Querys.getById(db, "Profiles", user_id)
    
    FireBaseDatabase.closeConnection()
    return profile_data