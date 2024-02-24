import telebot
import texts
from general_controller import GeneralController

general_controller = GeneralController()
token = general_controller.get_tg_admin_token()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, texts.GREETING_ADMIN_TEXT)


@bot.message_handler(commands=['getAmountOfUsers'])
def get_amount_of_users(message):
    date = None
    if message.text != '/getAmountOfUsers':
        date = message.text[18:]
        if general_controller.is_valid_date(date) is False:
            bot.send_message(message.chat.id, texts.INVALID_DATE)
            date = None
    amount = general_controller.get_amount_of_users(date)
    total = amount['total'][0][0]
    day = amount['day'][0][0]
    bot.send_message(message.chat.id, f'Всего: {total}\nВ выбранный день: {day}')


bot.polling(none_stop=True)
