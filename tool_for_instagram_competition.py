import os, instabot
from instabot import Bot 
from dotenv import load_dotenv
import re
import argparse
import sys

def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('name_of_page')
    return parser

def get_mentions(comment):
    mentions = re.findall(r"@([a-zA-Z0-9]{1,15})", str(comment['text']))
    return mentions

def get_likers_users(existing_users):
    for existing_user_id in existing_users:
        try:
            userid_applicant, applicant_user_name = existing_user_id
        except ValueError:
            pass 
        likers_user = bot.get_media_likers(userid_applicant)	
        if likers_user != userid_applicant:
            try:
                existing_users.remove(existing_user_id)
            except IndexError: 
                pass      
    return existing_users 

def get_followers(exist_and_likers_user):  
    followers_user = set(bot.get_user_followers(cmd_arguments.name_of_page))
    exist_and_likers_usersid = set(user_id[0] for user_id in exist_and_likers_user)    
    follower_ids = followers_user & exist_and_likers_usersid
    return follower_ids        

if __name__ == '__main__': 

    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    bot = Bot()
    bot.login(username = login, password = password)

    entered_links = createparser()
    cmd_arguments = entered_links.parse_args()

    post_id = bot.get_media_id_from_link(cmd_arguments.url)
    all_comments = bot.get_media_comments_all(post_id)
    
    comment_owner_username_with_mentions = []
    for comment in all_comments:
        try:
            mentions = get_mentions(comment)
        except TypeError: 
            pass             
        if mentions:
            applicant_user_name = comment['user']['username']
            username_and_mentions = (applicant_user_name, mentions)
            comment_owner_username_with_mentions.append(username_and_mentions) 

    existing_users = []
    for comment_owner_with_mention in comment_owner_username_with_mentions:
        comment_owner, comment_mentions = comment_owner_with_mention
        try:
            friend1_user_name, friend2_user_name = comment_mentions[:2]
        except ValueError:
            pass
        try:       
            friend2_user_id = bot.get_user_id_from_username(friend2_user_name)
            friend1_user_id = bot.get_user_id_from_username(friend1_user_name) 
        except TypeError: 
            pass         
        if friend1_user_id and friend2_user_id:
            try:	
                applicant_user_id = bot.get_user_id_from_username(comment_owner)
            except IndexError: 
                pass   	
            if applicant_user_id:
                username_and_id = (applicant_user_id, comment_owner)
                try: 		
                    existing_users.append(username_and_id)
                except IndexError: 
                    pass  

    exist_and_likers_user = get_likers_users(existing_users)
    follower_ids = get_followers(exist_and_likers_user)
    
    for number, userid in enumerate(follower_ids):
        name_of_user = bot.get_username_from_user_id(userid)
        print("{0}. {1}".format(number, name_of_user))
