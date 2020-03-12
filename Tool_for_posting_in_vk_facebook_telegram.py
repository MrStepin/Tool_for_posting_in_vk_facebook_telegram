import os
from dotenv import load_dotenv
import re
import argparse
import sys
import requests
import vk_api
import telegram

MESSAGE = "Test message"
PHOTO = "C:/Users/Stas/Desktop/1.png"

def post_to_vk(MESSAGE, PHOTO, vk_login,vk_password,vk_album_id,vk_group_id,vk_owner_id):
    session = vk_api.VkApi(vk_login, vk_password)
    session.auth(token_only=True)
    vk_get_api = session.get_api()
    photo_upload = vk_api.VkUpload(session)
    photo = photo_upload.photo(PHOTO, album_id=vk_album_id, group_id=vk_group_id)
    for photo_id in photo:
        uploaded_photo = photo_id["id"]
    vk_get_api.wall.post(message=MESSAGE, attachment="photo-{}_{}".format(vk_group_id, uploaded_photo) , owner_id=vk_owner_id)

def post_to_telegram(MESSAGE, PHOTO,telegram_chat_id,telegram_token):
    bot = telegram.Bot(token=telegram_token)
    bot.send_message(chat_id=telegram_chat_id, text=MESSAGE)
    bot.send_photo(chat_id=telegram_chat_id, photo=open(PHOTO, "rb"))


def post_to_facebook(MESSAGE, PHOTO, facebook_access_token):

    with open(PHOTO, "rb") as image_file:
        parameters={"message":MESSAGE, "access_token":facebook_access_token}
        files={"upload_file":PHOTO}
        response=requests.post("https://graph.facebook.com/v6.0/908375519577595/photos", params=parameters, files=files)
        response.raise_for_status()     

if __name__ == '__main__': 
    
    load_dotenv()
    vk_login = os.getenv("vk_login")
    vk_password = os.getenv("vk_password")
    vk_photo_in_group_id = os.getenv("vk_photo_in_group_id")
    vk_owner_id = os.getenv("vk_owner_id")
    vk_group_id = os.getenv("vk_group_id")
    vk_album_id = os.getenv("vk_album_id")
    telegram_token = os.getenv("telegram_token")
    telegram_chat_id = os.getenv("telegram_chat_id")
    facebook_access_token = os.getenv("facebook_access_token")

    post_to_vk(MESSAGE, PHOTO, vk_login,vk_password,vk_album_id,vk_group_id,vk_owner_id)
    post_to_telegram(MESSAGE, PHOTO, telegram_chat_id,telegram_token)
    post_to_facebook(MESSAGE, PHOTO, facebook_access_token)

    	