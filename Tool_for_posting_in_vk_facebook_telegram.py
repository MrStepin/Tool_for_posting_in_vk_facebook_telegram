import os
from dotenv import load_dotenv
import re
import argparse
import sys
import requests
import vk_api
import telegram

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    parser.add_argument('photo')
    return parser

def post_to_vk(vk_login,vk_password,vk_album_id,vk_group_id,vk_owner_id, photo, message):
    session = vk_api.VkApi(vk_login, vk_password)
    session.auth(token_only=True)
    vk_get_api = session.get_api()
    photo_upload = vk_api.VkUpload(session)
    photo = photo_upload.photo(photo, album_id=vk_album_id, group_id=vk_group_id)
    picture_vk_name="photo-{}_{}".format(vk_group_id, photo[0]["id"])
    vk_get_api.wall.post(message=message, attachment=picture_vk_name , owner_id=vk_owner_id)

def post_to_telegram(telegram_chat_id,telegram_token, photo, message):

    with open(photo, "rb") as photo:
        bot = telegram.Bot(token=telegram_token)
        bot.send_message(chat_id=telegram_chat_id, text=message)
        bot.send_photo(chat_id=telegram_chat_id, photo=photo)


def post_to_facebook(facebook_access_token, photo, message):

    with open(photo, "rb") as image_file:
        parameters={"message":message, "access_token":facebook_access_token}
        files={"upload_file":photo}
        response=requests.post("https://graph.facebook.com/v6.0/908375519577595/photos", params=parameters, files=files)
        response.raise_for_status()     

if __name__ == '__main__': 
    
    entered_args = create_parser()
    cmd_arguments = entered_args.parse_args()

    load_dotenv()
    vk_login = os.getenv("VK_LOGIN")
    vk_password = os.getenv("VK_PASSWORD")
    vk_owner_id = os.getenv("VK_OWNER_ID")
    vk_group_id = os.getenv("VK_GROUP_ID")
    vk_album_id = os.getenv("VK_ALBUM_ID")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    facebook_access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")

    photo = cmd_arguments.photo
    message = cmd_arguments.message
    
    post_to_vk(vk_login,vk_password,vk_album_id,vk_group_id,vk_owner_id, photo, message)
    post_to_telegram(telegram_chat_id,telegram_token, photo, message)
    post_to_facebook(facebook_access_token, photo, message)

    	