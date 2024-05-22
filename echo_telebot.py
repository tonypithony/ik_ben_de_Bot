#  conda create --name TELEBOT

# conda activate TELEBOT

# pip install pyTelegramBotAPI
# @ik_ben_de_bot

#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '<api_token from https://t.me/BotFather>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['document'])
def send_text(message):
    try:
        try:
            save_dir = message.caption
        except:
            save_dir = os.getcwd()
            s = "[!] you aren't entered directory, saving to {}".format(save_dir)
            bot.send_message(message.chat.id, str(s))
        file_name = message.document.file_name
        file_id = message.document.file_name
        file_id_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_id_info.file_path)
        src = file_name
        with open(save_dir + "/" + src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, "[*] File added:\nFile name - {}\nFile directory - {}".format(str(file_name), str(save_dir)))
    except Exception as ex:
        bot.send_message(message.chat.id, "[!] error - {}".format(str(ex)))


@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    try:
        try:
            save_dir = message.caption
        except:
            save_dir = os.getcwd()
            s = "[!] you aren't entered directory, saving to {}".format(save_dir)
            bot.send_message(message.chat.id, str(s))
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = save_dir + '/' + message.photo[1].file_id + '.jpg'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото добавлено")
    except Exception as ex:
        bot.send_message(message.chat.id, "[!] error - {}".format(str(ex)))


print("I'm working...")
bot.infinity_polling()