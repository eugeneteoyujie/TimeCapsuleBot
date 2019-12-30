import telepot
from telepot.loop import MessageLoop

bot = telepot.Bot("Your Token Here")

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        bot.sendMessage(chat_id,"HELLO")
  
  
MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)