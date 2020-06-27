from telethon.sync import TelegramClient, events
from tqdm import  tqdm
import os


api_id = #id
api_hash = #hash get id and hash from telegram api


with TelegramClient('name', api_id, api_hash) as client:
    messages = client.get_messages('https://t.me/codevita9', limit=50)
    for msg in tqdm(messages):
        msg.download_media(file=os.path.join('media', '<file_name>'))