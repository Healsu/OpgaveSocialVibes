from Database import FireBaseDatabase

def GetFromIndex(start_number):
    batch_size = 3
    print(start_number)
    db = FireBaseDatabase.getConnection()
    if start_number == "0":
        profiles_ref = db.child("Profiles").order_by_key().start_at(start_number).limit_to_first(batch_size).get()
    else:
        profiles_ref = db.child("Profiles").order_by_key().start_at(start_number).limit_to_first(batch_size+1).get()
        profiles_ref.popitem(last=False)
    
    FireBaseDatabase.closeConnection()
    return profiles_ref