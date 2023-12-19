from Database import FireBaseDatabase, Querys

def Get(event_ID):
    db = FireBaseDatabase.getConnection()

    event_object = Querys.getById(db, "Events", event_ID)

    event_participants_object = Querys.getById(db, "Event Participants", event_ID)
    events_ref_data = {
        "Admin": event_object.get("Admin"),
        "Latitude": float(event_object.get("Latitude")),
        "Longitude": float(event_object.get("Longitude")),
        "TimeStamp": event_object.get("TimeStamp"),
        "Title": event_object.get("Title")
    }
    FireBaseDatabase.closeConnection()
    return { "Event": events_ref_data, "Event Participants": event_participants_object }

def GetAll():
    db = FireBaseDatabase.getConnection()
    events_ref_data = {}
    events_ref = db.child("Events").get()

    events_participants_ref = db.child("Event Participants").get()
    
    FireBaseDatabase.closeConnection()
    for event_id, event_data in events_ref.items():
        data = {
            "Admin": event_data.get("Admin"),
            "Latitude": float(event_data.get("Latitude")),
            "Longitude": float(event_data.get("Longitude")),
            "TimeStamp": event_data.get("TimeStamp"),
            "Title": event_data.get("Title")
        }
        events_ref_data[event_id] = data

    return { "Event":events_ref_data, "Event Participants": events_participants_ref}