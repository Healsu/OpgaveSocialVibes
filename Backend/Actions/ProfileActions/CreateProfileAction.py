from Database import FireBaseDatabase
from Model.Profile import Profile

def saveProfile(data):
    collectionName = 'Profiles'

    db = FireBaseDatabase.getConnection()

    #create Model to reinforce layout of the object in the database:
    profile = Profile(data["Name"])

    profiles_ref = db.child(collectionName)

    # Push the data to the "users" node (auto-generated ID)
    new_data_ref = profiles_ref.push(profile.toDict())

    print(f"Added data with key: {new_data_ref.key}")

    FireBaseDatabase.closeConnection()
