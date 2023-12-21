from Database import FireBaseDatabase, Querys

def Get(event_ID):
    db = FireBaseDatabase.getConnection()

    event_object = Querys.getById(db, "Events", event_ID)

    event_participants_object = db.child("Event Participants").child(event_ID).get()
    events_ref_data = {
        "Admin": event_object.get("Admin"),
        "Latitude": float(event_object.get("Latitude")),
        "Longitude": float(event_object.get("Longitude")),
        "TimeStamp": event_object.get("TimeStamp"),
        "Title": event_object.get("Title"),
        "Description": event_object.get("Description"),
        'StartDate': event_object.get("StartDate"),
        'StartTime': event_object.get("StartTime"),
        'StopDate': event_object.get("StopDate"),
        'StopTime': event_object.get("StopTime"),
        'Adress': event_object.get("Adress")
    }
    FireBaseDatabase.closeConnection()
    return { "Event": events_ref_data, "Event Participants": event_participants_object }

def GetAll():
    db = FireBaseDatabase.getConnection()
    events_ref_data = {}
    events_ref = db.child("Events").get()
    
    FireBaseDatabase.closeConnection()
    for event_id, event_data in events_ref.items():
        data = {
            "Id": event_id,
            "Latitude": float(event_data.get("Latitude")),
            "Longitude": float(event_data.get("Longitude")),
            "Title": event_data.get("Title"),
        }
        events_ref_data[event_id] = data

    return { "Event":events_ref_data}