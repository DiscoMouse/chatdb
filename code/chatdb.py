import datetime
import time
from pymongo import MongoClient
from chat_downloader import ChatDownloader
import requests

def is_live(channel_id):
    # Try to fetch the YouTube channel page
    try:
        response = requests.get('https://www.youtube.com/channel/' + channel_id)
        # If "hqdefault_live.jpg" is in the response, the channel is live
        if "hqdefault_live.jpg" in response.text:
            return True
        else:
            return False
    except Exception as err:
        print('Something went wrong:', err)
        return False

def monitor():
    while True:
        try:
            if live == True:
                print("Stream is live now! Recording chat!")
                chatdb(url)
                break
            else:
                time.sleep(5)
        except Exception as err:
            print('Something went wrong:', err)
            pass

def chatdb(url):
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client.slappedham
    collection = db.messages
    chat = ChatDownloader().get_chat(url)
    for message in chat:                        # iterate over messages
        chat.print_formatted(message)           # print the formatted message
        logtime = datetime.datetime.utcnow()
        message["logtime"] = logtime
        message["Video URL"] = url
        messages = db.messages
        post_msg = messages.insert_one(message).inserted_id
        post_msg

 
# Putting it all together

# The YouTube Live channel name you wish to target.
# Replace CHAN_NAME in the url below with the channel you wish to monitor.

url = "https://www.youtube.com/c/CHAN_NAME/live"

# The YouTube channel_id 

channel_id = ""

# Check if stream is live if now wait 5 seconds try again, if live record the chat to the database.
live = (is_live(channel_id))
print("Waiting for stream to go live press ctrl C to exit early.")
monitor()
