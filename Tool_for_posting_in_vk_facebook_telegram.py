import os
from dotenv import load_dotenv
import re
import argparse
import sys
import requests
import vk_api
import telegram

def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    parser.add_argument('photo')
    return parser

def post_to_vk(vk_login,vk_password,vk_album_id,vk_group_id,vk_owner_id):
    session = vk_api.VkApi(vk_login, vk_password)
    session.auth(token_only=True)
    vk_get_api = session.get_api()
    photo_upload = vk_api.VkUpload(session)
    photo = photo_upload.photo(cmd_arguments.photo, album_id=vk_album_id, group_id=vk_group_id)
    for photo_id in photo:
        uploaded_photo = photo_id["id"]
    vk_get_api.wall.post(message=cmd_arguments.message, attachment="photo-{}_{}".format(vk_group_id, uploaded_photo) , owner_id=vk_owner_id)

def post_to_telegram(telegram_chat_id,telegram_token):

    with open(cmd_arguments.photo, "rb") as photo:
        bot = telegram.Bot(token=telegram_token)
        bot.send_message(chat_id=telegram_chat_id, text=cmd_arguments.message)
        bot.send_photo(chat_id=telegram_chat_id, photo=photo)


def post_to_facebook(facebook_access_token):

    with open(cmd_arguments.photo, "rb") as image_file:
        parameters={"message":cmd_arguments.message, "access_token":facebook_access_token}
        files={"upload_file":cmd_arguments.photo}
        response=requests.post("https://graph.facebook.com/v6.0/908375519577595/photos", params=parameters, files=files)
        response.raise_for_status()     

if __name__ == '__main__': 
    
    entered_args = createparser()
    cmd_arguments = entered_args.parse_args()

    load_dotenv()
    vk_login = os.getenv("vk_login")
    vk_password = os.getenv("vk_password")
    vk_owner_id = os.getenv("vk_owner_id")
    vk_group_id = os.getenv("vk_group_id")
    vk_album_id = os.getenv("vk_album_id")
    telegram_token = os.getenv("telegram_token")
    telegram_chat_id = os.getenv("telegram_chat_id")
    facebook_access_token = os.getenv("facebook_access_token")
    
    post_to_vk(vk_login,vk_password,vk_album_id,vk_group_id,vk_owner_id)
    post_to_telegram(telegram_chat_id,telegram_token)
    post_to_facebook(facebook_access_token)

    	