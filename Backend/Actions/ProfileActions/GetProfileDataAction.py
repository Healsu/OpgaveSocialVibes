from Database import FireStore, Querys
from Model.Profile import Profile

def getProfile(id):
    db = FireStore.getConnection()
    
    profile_data = Querys.getById(db, "Profiles", id)
    
    FireStore.closeConnection()
    return profile_data