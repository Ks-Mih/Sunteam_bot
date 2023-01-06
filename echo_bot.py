import json

from telebot import TeleBot

import quiz
from settings import MY_BOT_TOKEN
from db_names import add_to_db
import keyboards
import texts

bot = TeleBot(MY_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Рады тебя видеть=)", reply_markup=keyboards.menuKeyboard)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == texts.MENU_ABOUT_US:
        bot.send_message(message.chat.id, text=texts.IN_DEVELOPMENT)
    elif message.text == texts.MENU_TEST:
        quiz.question(bot, message.chat.id, 0)
    elif message.text == texts.MENU_ACCOUNT:
        bot.send_message(message.chat.id, text=texts.IN_DEVELOPMENT)
    elif message.text == texts.MENU_PEOPLE_INFO:
        bot.send_message(message.chat.id, text=texts.IN_DEVELOPMENT)
    elif message.text == texts.MENU_RATES:
        bot.send_message(message.chat.id, text=texts.IN_DEVELOPMENT)
    else:
        bot.send_message(message.chat.id, text=texts.IN_DEVELOPMENT)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        data = json.loads(call.data)
        if data['tp'] == 'qz':
            add_to_db(data)
            quiz.question(bot, data['id'], data['ind'] + 1)


bot.infinity_polling()
