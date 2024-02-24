import telebot

import texts
from general_controller import GeneralController
from texts import *

general_controller = GeneralController()
token = general_controller.get_tg_token()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, texts.GREETING_TEXT)


@bot.message_handler(commands=["termsOfUse"])
def terms_of_use(message):
    bot.send_message(message.chat.id, texts.TERMS_OF_USE)


@bot.message_handler(content_types=['text'])
def ai_answer(message):
    answer = general_controller.get_ai_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
