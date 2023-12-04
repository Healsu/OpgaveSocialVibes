from Database import FireBaseDatabase

def get():
    try:
        db = FireBaseDatabase.getConnection()

        profiles = db.child("Profiles").get()


        FireBaseDatabase.closeConnection()
        return profiles
    except:
        raise Exception("something went wrong")