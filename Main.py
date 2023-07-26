from colorama import init as colorama_init
from colorama import Fore
from discum import Client
import time
import os
import requests
import json

with open('config.json') as f:
	config = json.load(f)

token = config.get('token')
api_key = config.get('api_key')
language = config.get('language')

colorama_init()

print(Fore.RED + " _                    _           ")
print(Fore.RED + "| |    __ _  ___  ___| |__  _   _ ")
print(Fore.RED + "| |   / _` |/ _ \/ __| '_ \| | | |")
print(Fore.RED + "| |__| (_| | (_) \__ \ | | | |_| |")
print(Fore.RED + "|_____\__,_|\___/|___/_| |_|\__,_|")
                                  
print("")
print(Fore.YELLOW + "Rest in peace Laoshu505000")
time.sleep(.2)
print(Fore.GREEN + "Credits to xawxow on github")
time.sleep(.3)
print("Now loading into the Laoshu Translator")
print(Fore.RESET)
time.sleep(.5)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
os.system('cls')
time.sleep(2)

print("Welcome to Laoshu Translator!")
print("_____________________________")

translator_api_url = "https://translate.yandex.net/api/v1.5/tr.json/translate"

translator_api_key = api_key

client = Client(token=token)

@client.gateway.command
def on_message(resp):
    data = resp.parsed.auto()

    if 'author' in data and data['author'].get('id') == uid
        if 'content' in data:
            message = data['content']
            print('Received message:', message)
            translated_message = translate_message(message)
            print('Translated message:', translated_message)
            edit_message(data, translated_message)

def translate_message(message):
    params = {
        "key": translator_api_key,
        "text": message,
        "lang": ('en',language)
    }

    response = requests.get(translator_api_url, params=params)
    translated_data = response.json()

    translated_message = translated_data['text'][0]

    return translated_message

def edit_message(data, translated_message):
    message_id = data['id']
    channel_id = data['channel_id']
    client.editMessage(channel_id, message_id, translated_message)

client.gateway.run(auto_reconnect=True)
