from Database import FireBaseDatabase


def get(user_id):
    db = FireBaseDatabase.getReferenceFromConnection("Chatrooms")

    # Query to get all chatrooms where the type is equal to 'Community'
    query_result = db.order_by_child("Type").equal_to("Community").get()

    return query_result
