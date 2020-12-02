import telebot
import time

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(content_types=['text'])
def onMessageSend(message):
    if message.chat.type != 'private':
        if bot.get_chat_member(message.chat.id, message.from_user.id).status == "left" \
                and not bot.get_chat_member(message.chat.id, message.from_user.id).user.is_bot \
                and str(message.from_user.username) != "None":
            iid = bot.reply_to(message, "@" + str(message.from_user.username)
                               + ", пожалуйства войдите в чат для общения.").id

            bot.delete_message(message.chat.id, message.id)

            timing = time.time()
            while True:
                if time.time() - timing > 5.0:
                    timing = time.time()
                    bot.delete_message(message.chat.id, iid)


bot.polling(none_stop=True)
