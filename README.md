Tool_for_posting_in_vk_facebook_telegram
=====================
 
This script posts message with photo to vk.com, facebook.com and telegram channel at the same time.  

Python3 should be installed.  
Use pip to install dependencies:  
```pip install -r requirements.txt```

How to use this script:  
* Create file  ```.env``` with you data.  
VK login, password, group id, album id.   
Telegram token and chat_id.  
Facebook token.   

Like this:  
```vk_login="57"```  
```vk_password="qx"```  
```vk_owner_id="-2090"```  
```vk_group_id="1090"```  
```vk_album_id="2745"```  
```telegram_token="11438:AAHyWU"```  
```telegram_chat_id="@Eduhon"```  
```facebook_access_token=EAALcfYf```  

* Execute this script in CMD with message and path to image on you PC as arguments.
For example:  
```python Tool_for_posting_in_vk_facebook_telegram.py "Nice day!" "C:/Users/S/Desktop/1.png"```

Script will work for several seconds and after that you will see message with photo in you groups in vk and facebook and telegram channel.
