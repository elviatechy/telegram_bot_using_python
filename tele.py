from telegram import *
from telegram.ext import *

bot = Bot("7196164913:AAGuFDBVI-GJ8k3bAJSMpr-jkKLOQ-Z6S1s")
#print(bot.get_me())
updater = Updater("7196164913:AAGuFDBVI-GJ8k3bAJSMpr-jkKLOQ-Z6S1s", use_context=True)

dispatcher= updater.dispatcher


def test_func(update:Update, context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text ="tutorial link : https://youtu.be/Tm5u97I7OrM",
    )
start_value = CommandHandler('motion_detection',test_func)

dispatcher.add_handler(start_value)

updater.start_polling()
