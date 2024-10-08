import os
import sys
import requests
import tkinter as tk
from tkinter import messagebox
import yaml
import time

#load .yml file
with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

print(config)

# Config
TEXT = config.get("text")
EMOJI = config.get("emoji")
EXPIRE_IN_MINUTES = config.get("expire_in_minutes")
EXPIRATION = int(time.time()) + EXPIRE_IN_MINUTES * 60  # Gets current time in UNIX timestamp then adds however many minutes.

slack_token = config.get("slack_oauth_token")
print(slack_token)
url = "https://slack.com/api/users.profile.set"

headers = {
    "Authorization": f"Bearer {slack_token}",
    "Content-Type": "application/json; charset=utf-8"
}

def set_status(text, emoji, expiration):
    data = {
        "profile": {
            "status_text": text,
            "status_emoji": emoji,
            "status_expiration": expiration
        }
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    print(response_json)

    if response_json.get("ok"):
        show_popup("Success", "Status updated successfully!")
    else:
        show_popup("Error", response_json["error"])

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()

def main():
    set_status(TEXT, EMOJI, EXPIRATION)

if __name__ == "__main__":
    main()


