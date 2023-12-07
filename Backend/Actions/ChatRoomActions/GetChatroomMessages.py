from Database import FireBaseDatabase, FireBaseStorage
import base64
import zlib

def getMessages(chatroom_id):
    try:
        # retrieve the data
        db = FireBaseDatabase.getConnection()
        chatroom_ref = db.child(f"Chatrooms/{chatroom_id}")
        chatroom_participants_ref = db.child(f"Chatroom Participants/{chatroom_id}") 
        chatroom_messages_ref = db.child(f"Chatroom Messages/{chatroom_id}")

        chatroom_data = chatroom_ref.get()
        chatroom_participants_data = chatroom_participants_ref.get()
        chatroom_messages_data = chatroom_messages_ref.get()
        FireBaseDatabase.closeConnection()

        messages = {}
        
        # get the image if there is one
        bucket = FireBaseStorage.getConnection()

        for key, value in chatroom_messages_data.items():
            # the data into variables
            message_key = key
            image_url = value.get('ImageURL', 'N/A')
            message = value.get('Message')
            ractions = value.get('Reactions')
            sender_id = value.get('SenderId')
            time_stamp = value.get('TimeStamp')
            is_seen = value.get('isSeen')

            if image_url != 'N/A':
                # fill the form data object with each iteration
                blob_path = f"Messages/{image_url}"
                image_blob = bucket.blob(blob_path)
                
                try:
                    image_data = image_blob.download_as_bytes()
                    compressed_image_data = zlib.compress(image_data)
                    base64_image = base64.b64encode(compressed_image_data).decode('utf-8')

                    messages[message_key] ={"Image": base64_image,
                                            "Message": message,
                                            "Reactions": ractions,
                                            "SenderId": sender_id,
                                            "TimeStamp": time_stamp,
                                            "isSeen": is_seen}
                    #testing to see if the image is found------------------------
                    # plt.imshow(image)
                    # plt.show()
                    
                except Exception as e:
                    FireBaseStorage.closeConnection()
                    print(f"Error downloading image: {e}")
            else:
                # For messages without pictures
                messages[message_key] ={"Image": "N/A",
                                        "Message": message,
                                        "Reactions": ractions,
                                        "SenderId": sender_id,
                                        "TimeStamp": time_stamp,
                                        "isSeen": is_seen}

        FireBaseStorage.closeConnection()
        return messages
    except Exception as e:
        raise Exception(f"Something went wrong: {e}")