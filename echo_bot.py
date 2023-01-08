import json

from telebot import TeleBot

from modules import quiz
from settings import MY_BOT_TOKEN, CHAT_ID
import connection_to_db.db_repository as db
from elements import keyboards
import texts

bot = TeleBot(MY_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    db.add_user(message.chat.id, message.from_user.username)

    bot.delete_message(message.chat.id, message.message_id)
    button_menu(message.chat.id)


@bot.message_handler(commands=['persons'])
def send_person_info(message):
    if message.chat.id == CHAT_ID:
        print("ok")
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['chat_id'])
def send_person_info(message):
    print(message.chat.id)
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def func(message):
    bot.delete_message(message.chat.id, message.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        data = json.loads(call.data)
        if data['type'] == 'quiz':
            if data.get('answer'):
                db.add_answer_to_quiz(chat_id=call.message.chat.id, question_id=data['index'], answer=data['answer'])
            button_quiz(call.message.chat.id, data['index'] + 1)
        if data['type'] == 'menu':
            callback_menu(call.message.chat.id, data['button'])


def callback_menu(chat_id, button):
    if button == 'about_us':
        button_about_us(chat_id)
    elif button == 'rates':
        button_rates(chat_id)
    elif button == 'account':
        button_account(chat_id)
    elif button == 'people_info':
        button_people_info(chat_id)
    elif button == 'quiz':
        button_start_quiz(chat_id)
    elif button == 'menu':
        button_menu(chat_id)
    else:
        print('mistake')


def button_menu(chat_id):
    main_photo = open('photos/main_photo.png', 'rb')
    m0_ind = bot.send_photo(chat_id=chat_id,
                            photo=main_photo,
                            caption=texts.MENU_TEXT_ABOUT_US,
                            reply_markup=keyboards.menu_keyboard_info(),
                            parse_mode="Markdown"
                            ).message_id
    quiz_photo = open('photos/quiz_main_photo.png', 'rb')
    m1_ind = bot.send_photo(chat_id=chat_id,
                            photo=quiz_photo,
                            caption=texts.MENU_TEXT_QUIZ,
                            reply_markup=keyboards.menu_keyboard_quiz(),
                            parse_mode="Markdown"
                            ).message_id
    restructure_messages(chat_id, [m0_ind, m1_ind])


def button_about_us(chat_id):
    in_development(chat_id)


def button_rates(chat_id):
    in_development(chat_id)


def button_account(chat_id):
    in_development(chat_id)


def button_people_info(chat_id):
    in_development(chat_id)


def in_development(chat_id):
    in_development_photo = open('photos/in_development.png', 'rb')
    m0_ind = bot.send_photo(chat_id=chat_id,
                            photo=in_development_photo,
                            caption=texts.IN_DEVELOPMENT,
                            reply_markup=keyboards.menu_or_quiz_keyboard(),
                            parse_mode="Markdown"
                            ).message_id
    restructure_messages(chat_id, [m0_ind])


def button_start_quiz(chat_id):
    db.add_chat_to_db(chat_id)
    button_quiz(chat_id, 0)


def button_quiz(chat_id, question):
    message_id = quiz.question(bot=bot, chat_id=chat_id, index=question)
    restructure_messages(chat_id, [message_id])


def restructure_messages(chat_id, messages_id):
    delete_all_messages(chat_id)
    db.add_messages_id(chat_id, messages_id)


def delete_all_messages(chat_id):
    for message_id in db.get_messages_id(chat_id):
        try:
            bot.delete_message(chat_id, message_id)
        except:
            print("nothing")
    db.delete_messages_info(chat_id)


print('бот запущен')
bot.infinity_polling()
