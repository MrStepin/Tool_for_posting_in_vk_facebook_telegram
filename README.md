Tool_for_posting_in_vk_facebook_telegram
=====================
 
This script posts message with photo to vk.com, facebook.com and telegram channel at the same time.  

## Environment:  
Python3 should be installed.  
### Requirements:  
Use pip to install dependencies:  
```pip install -r requirements.txt```

## Environment variables:   
Create file  ```.env``` with you data:  
VK login, password, group id, album id.   
Telegram token and chat_id.  
Facebook token.   
Like this:  
```VK_LOGIN="57"```  
```VK_PASSWORD="qx"```  
```VK_OWNER_ID="-2090"```  
```VK_GROUP_ID="1090"```  
```VK_ALBUM_ID="2745"```  
```TELEGRAM_TOKEN="11438:AAHyWU"```  
```TELEGRAM_CHAT_ID="@Eduhon"```  
```FACEBOOK_ACCESS_TOKEN=EAALcfYf```  

## Run:  
Execute this script in CMD with message and path to image on you PC as arguments.
For example:  
```python Tool_for_posting_in_vk_facebook_telegram.py "Nice day!" "C:/Users/S/Desktop/1.png"```

Script will work for several seconds and after that you will see message with photo in you groups in vk and facebook and telegram channel.
