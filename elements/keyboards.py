from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from json import dumps
import texts


def menu_keyboard_info():
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(texts.MENU_ABOUT_US,
                                callback_data=dumps({'type': 'menu', 'button': 'about_us'}))
    btn2 = InlineKeyboardButton(texts.MENU_RATES,
                                callback_data=dumps({'type': 'menu', 'button': 'rates'}))
    keyboard.row(btn1, btn2)
    keyboard.add(InlineKeyboardButton(texts.MENU_ACCOUNT,
                                      callback_data=dumps({'type': 'menu', 'button': 'account'})))
    return keyboard


def menu_keyboard_quiz():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(texts.MENU_PEOPLE_INFO,
                                      callback_data=dumps({'type': 'menu', 'button': 'people_info'})))
    keyboard.add(InlineKeyboardButton(texts.MENU_QUIZ,
                                      callback_data=dumps({'type': 'menu', 'button': 'quiz'})))
    return keyboard


def inline_keyboard_1_to_5(question_index):
    answers = InlineKeyboardMarkup()
    data = {'type': 'quiz', 'index': question_index, 'answer': 1}
    btn1 = InlineKeyboardButton(text="1", callback_data=dumps(data))
    data['answer'] = 2
    btn2 = InlineKeyboardButton(text="2", callback_data=dumps(data))
    data['answer'] = 3
    btn3 = InlineKeyboardButton(text="3", callback_data=dumps(data))
    data['answer'] = 4
    btn4 = InlineKeyboardButton(text="4", callback_data=dumps(data))
    data['answer'] = 5
    btn5 = InlineKeyboardButton(text="5", callback_data=dumps(data))
    answers.row(btn1, btn2, btn3, btn4, btn5)
    answers.add(InlineKeyboardButton(text=texts.BACK_TO_MENU,
                                     callback_data=dumps({'type': 'menu', 'button': 'menu'})))
    return answers


def menu_or_quiz_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(texts.BACK_TO_MENU,
                                      callback_data=dumps({'type': 'menu', 'button': 'menu'})))
    keyboard.add(InlineKeyboardButton(texts.MENU_QUIZ,
                                      callback_data=dumps({'type': 'menu', 'button': 'quiz'})))
    return keyboard


def inline_keyboard_end_quiz():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(texts.END_QUIZ,
                                      callback_data=dumps({'type': 'menu', 'button': 'menu'})))
    return keyboard


def start_or_back_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(texts.BACK_TO_MENU,
                                      callback_data=dumps({'type': 'menu', 'button': 'menu'})))
    keyboard.add(InlineKeyboardButton(texts.START_QUIZ,
                                      callback_data=dumps({'type': 'quiz', 'index': 0})))
    return keyboard
