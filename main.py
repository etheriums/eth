import os
import requests

token = ""
guild = None
channel = input("Channel -> ")
print()

def send(content):
    json = {
        "content": content
    }
    r = requests.post("https://discord.com/api/channels/%s/messages" % (channel), json=json, headers={"Authorization": token})
    return r.json()

def reply(message_id, content):
    json  = {
        "content": content,
        "tts": False,
        "message_reference":{
            "guild_id": guild,
            "channel_id": channel,
            "message_id":message_id
        }
    }
    r = requests.post("https://discord.com/api/channels/%s/messages" % (channel), json=json, headers={"Authorization": token})
    return r.json()

def start():
    os.system("clear")
    first = send(input("First message -> "))
    print(first)
    second = reply(first["id"], input("Second reply -> "))
    print(second)
    while True:
        exploit = reply(second["id"], input("Message -> "))
        os.system("clear")
        
if __name__ == "__main__":
    start()
