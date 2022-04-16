# File-sharing-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
  <a href="https://t.me/CodeXBotz">
    <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://t.me/CodeXBotz">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://t.me/codexbotzsupport">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/CodeXBotz/File-Sharing-Bot?style=social">
  </a>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/fork">
    <img src="https://img.shields.io/github/forks/CodeXBotz/File-Sharing-Bot?label=Fork&style=social">
  </a>  
</p>


Telegram Bot to store Posts and Documents and it can Access by Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

##

**If you need any more modes in repo or If you find out any bugs, mention in [@codexbotzsupport ](https://www.telegram.dog/codexbotzsupport)**

### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku directly.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
**BEFORE YOU DEPLOY ON HEROKU, YOU SHOULD FORK THE REPO AND CHANGE ITS NAME TO ANYTHING ELSE**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>
<a href="https://youtu.be/LCrkRTMkmzE">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>
**Check This Tutorial Video on YouTube for any Help**<br>
**Thanks to [Erich](https://t.me/ErichDaniken) and his [InFoTel](https://t.me/InFoTel_Group) for this Video**

#### Deploy on Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FCodeXBotz%2FFile-Sharing-Bot&plugins=postgresql&envs=TG_BOT_TOKEN%2COWNER_ID%2CAPP_ID%2CAPI_HASH%2CCHANNEL_ID%2CFORCE_SUB_CHANNEL%2CSTART_MESSAGE%2CFORCE_SUB_MESSAGE%2CADMINS&optionalEnvs=ADMINS&TG_BOT_TOKENDesc=Your+Bot+token%2C+Get+it+from+%40Botfather&OWNER_IDDesc=An+integer+of+consisting+of+your+owner+ID&APP_IDDesc=your+app+id%2C+take+it+from+my.telegram.org&API_HASHDesc=your+api+hash%2C+take+it+from+my.telegram.org&CHANNEL_IDDesc=make+a+channel+%28database+channel%29%2C+then+make+the+bot+as+admin+in+channel%2C+and+it%27s+id&FORCE_SUB_CHANNELDesc=id+of+the+channel+or+group%2C+if+you+want+enable+force+sub+feature+else+put+0&START_MESSAGEDesc=Optional%3A+start+message+of+bot%2C+use+HTML+parsemode+format&FORCE_SUB_MESSAGEDesc=Optional%3A+Force+Sub+message+of+bot%2C+use+HTML+parsemode+format&ADMINSDesc=A+space+separated+list+of+user_ids+of+Admins%2C+they+can+only+create+links&TG_BOT_TOKENDefault=1250450587&CHANNEL_IDDefault=-100&FORCE_SUB_CHANNELDefault=0&START_MESSAGEDefault=Hello+%7Bfirst%7D%5Cn%5CnI+can+store+private+files+in+Specified+Channel+and+other+users+can+access+it+from+special+link.&FORCE_SUB_MESSAGEDefault=Hello+%7Bfirst%7D%5Cn%5Cn%3Cb%3EYou+need+to+join+in+my+Channel%2FGroup+to+use+me%5Cn%5CnKindly+Please+join+Channel%3C%2Fb%3E&referralCode=CodeXBotz)

#### Deploy in your VPS
````bash
git clone https://github.com/CodeXBotz/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users
```

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `API_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


## Support   
Join Our [Telegram Group](https://www.telegram.dog/codexbotzsupport) For Support/Assistance And Our [Channel](https://www.telegram.dog/codexbotz) For Updates.   
   
Report Bugs, Give Feature Requests There..   

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Our Support Group Members

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/CodeXBotz/File-Sharing-Bot/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Star this Repo if you Liked it ⭐⭐⭐**

