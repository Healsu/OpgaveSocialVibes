from Database import FireBaseDatabase, Querys
from Model.Event import Event

def create(data):
    db = FireBaseDatabase.getConnection()
    lat = data["Latitude"]
    lng = data["Longitude"]
    title = data["Title"]
    description = data["Description"]
    start_date = data["StartDate"]
    stop_date = data["StopDate"]
    adress = data["adress"]
    admin_object = Querys.getById( db, "Profiles", data["Admin"])
    participants_list = [admin_object]

    event_object = Event(lat, lng, admin_object, title, description, start_date, stop_date, adress)

    #create objects in json database
    event_ref = db.child('Events')

    event_ref_data = event_ref.push(event_object.toDict())

    #get the id for the object
    event_ref_id = event_ref_data.key

    #use it to create the other json objects
    event_participants_ref = db.child('Event Participants')
    event_participants_ref.child(event_ref_id).set(participants_list)

    FireBaseDatabase.closeConnection()