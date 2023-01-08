from telebot import TeleBot
from texts import QUESTION_0_TYPE, QUESTION_1_EVENT, QUESTION_2_WAIT, QUESTION_3_PLAN, QUESTION_4_COUNT, QUEST_INTRO
from elements.keyboards import inline_keyboard_1_to_5, start_or_back_keyboard
from connection_to_db.db_names import COLUMN_Q_COUNT, COLUMN_Q_EVENT, COLUMN_Q_TYPE, COLUMN_Q_PLAN, COLUMN_Q_WAIT

QUEST = [
    {'text': QUEST_INTRO, 'type': 'start_or_back'},
    {"column_name_in_db": COLUMN_Q_TYPE, 'text': QUESTION_0_TYPE, 'type': '1_to_5'},
    {"column_name_in_db": COLUMN_Q_EVENT, 'text': QUESTION_1_EVENT, 'type': '1_to_5'},
    {"column_name_in_db": COLUMN_Q_WAIT, 'text': QUESTION_2_WAIT, 'type': '1_to_5'},
    {"column_name_in_db": COLUMN_Q_PLAN, 'text': QUESTION_3_PLAN, 'type': '1_to_5'},
    {"column_name_in_db": COLUMN_Q_COUNT, 'text': QUESTION_4_COUNT, 'type': '1_to_5'},
]


def question(bot: TeleBot, chat_id, index: int):
    if 0 <= index < len(QUEST):
        if QUEST[index].get('type') == '1_to_5':
            return quest_1_to_5(bot, chat_id, index)
        elif QUEST[index].get('type') == 'start_or_back':
            return start_or_back(bot, chat_id, index)
    else:
        return bot.send_message(chat_id=chat_id,
                                text="Hello").message_id


def quest_1_to_5(bot: TeleBot, chat_id, index: int):
    return bot.send_message(chat_id=chat_id,
                            text=QUEST[index].get('text'),
                            parse_mode="Markdown",
                            reply_markup=inline_keyboard_1_to_5(index)).message_id


def start_or_back(bot: TeleBot, chat_id, index: int):
    quiz_best_photo = open('photos/quiz_best_surprise.png', 'rb')
    return bot.send_photo(chat_id=chat_id,
                          photo=quiz_best_photo,
                          caption=QUEST[index].get('text'),
                          parse_mode="Markdown",
                          reply_markup=start_or_back_keyboard()).message_id
