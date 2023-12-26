from Database import FireBaseDatabase, Querys


def get(user_Id):
    try:
        db = FireBaseDatabase.getConnection()
        events = db.child("Event Participants").get().items()
        event_objects = {}
        for event in events:
            for profile in event[1]:
                if(profile["id"] == user_Id):
                    event_data = db.child("Events").child(event[0]).get()
                    data = {
                            'EventID': event[0],
                            'Adress': event_data.get("Adress", None),
                            'Description': event_data.get("Description", None),
                            'Latitude': event_data.get("Latitude", None),
                            'Longitude': event_data.get("Longitude", None),
                            'StartDate': event_data.get("StartDate", None),
                            'StartTime': event_data.get("StartTime", None),
                            'StopDate': event_data.get("StopDate", None),
                            'StopTime': event_data.get("StopTime", None),
                            'TimeStamp': event_data.get("TimeStamp", None),
                            'Title': event_data.get("Title", None)
                        }
                    event_objects[event[0]] = data 
        FireBaseDatabase.closeConnection()
        return event_objects
    except:
        FireBaseDatabase.closeConnection()