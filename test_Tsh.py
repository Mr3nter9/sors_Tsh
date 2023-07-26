from time import sleep; import requests
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.sync import TelegramClient , functions , events
import asyncio
import os
id='5229914714'
token='6183317549:AAGB5jAoTSGSc0M0Y_8WR7kEa7oYbyjshM0'
numb_s ='1'
use = ["dex34bot"]
led=TelegramClient('Tshek', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
led.start()
led.send_message('botfather', '/newbot')
led.send_message('botfather', 'Dex')
def Tsh():
 while True:
  i = 0
  while True:
   i+=+1
   if i == 100:
    sleep(1.4)
    break

   while True:
    sleep(0.05)
    for user in use:
     req = requests.get(f"https://t.me/{user}")
     if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
      led.send_message('botfather', user)

     else:
      print(f"NOOO : {user}" +' '+ str(i))
    break

@led.on(events.NewMessage(outgoing=True, pattern="x"))
async def spammer(event):
 while True:
  i = 0
  while True:
   i+=+1
   if i == 100:
    sleep(1.4)
    break

   while True:
    sleep(0.05)
    for user in use:
     req = requests.get(f"https://t.me/{user}")
     if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
      await led.send_message('botfather', user)

     else:
      print(f"NOOO : {user}" +' '+ str(i))
    break


led.run_until_disconnected()