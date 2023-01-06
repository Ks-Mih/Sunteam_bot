from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts import QUESTION_0, QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4
from json import dumps

QUEST_TXT = [QUESTION_0, QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4]


# Автоматически создаем вопрос по переданному индексу
# 1. Обращаемся к массиву вопросов и ответов(QUEST_TXT) из файла texts
# 2. Если строка с таким номером есть в массиве, то под [0] индексом информация о вопросе, под [1] ответы
# 3. Создаем меню с вопросами при помощи метода __create_answers_markup, передав индекс вопроса
# 4. Отправляем вопрос, добавляя имя вопроса и меню
def question(bot: TeleBot, chat_id, index: int):
    if 0 <= index < len(QUEST_TXT):
        answers = __create_answers_markup(index, chat_id)
        bot.send_message(chat_id, QUEST_TXT[index][1], reply_markup=answers)
    else:
        answers = __create_exit_markup()
        bot.send_message(chat_id, text="Hello", reply_markup=answers)


def __create_answers_markup(index, chat_id):
    answers = InlineKeyboardMarkup(row_width=1)
    for i in range(5):
        answers.add(
            InlineKeyboardButton(
                text=i,
                callback_data=dumps({'tp': 'qz', 'id': chat_id, 'ind': index, 'ans': i})))
    return answers


def __create_exit_markup():
    answers = InlineKeyboardMarkup()
    answers.add(InlineKeyboardButton(text='Выйти', callback_data='exit'))
    return answers
