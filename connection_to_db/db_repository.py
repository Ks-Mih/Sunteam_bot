import datetime
import sqlite3
from settings import SQLITE3_ADDRES
from connection_to_db.db_names import *
from connection_to_db.db_query import insert_or_ignore_query, update_query, insert_query, select_with_where_query, \
    delete_query, select_query
from modules.quiz import QUEST

conn = sqlite3.connect(SQLITE3_ADDRES, check_same_thread=False)
cursor = conn.cursor()


def add_user(chat_id, user_name):
    query = insert_or_ignore_query(table_name=TABLE_USERS_INFO,
                                   columns=[COLUMN_CHAT_ID, COLUMN_UI_USER_NAME, COLUMN_CREATION_DATE])
    data = [chat_id, user_name, datetime.datetime.now()]
    cursor.execute(query, data)
    conn.commit()


def add_chat_to_db(chat_id):
    query = insert_or_ignore_query(table_name=TABLE_QUIZ_SURPRISE_TYPE,
                                   columns=[COLUMN_CHAT_ID, COLUMN_CREATION_DATE])
    data = [chat_id, datetime.datetime.now()]
    cursor.execute(query, data)
    conn.commit()


def add_answer_to_quiz(chat_id, question_id, answer):
    query = update_query(table_name=TABLE_QUIZ_SURPRISE_TYPE,
                         columns=[QUEST[question_id]["column_name_in_db"], COLUMN_UPDATE_DATE],
                         name_id_column=[COLUMN_CHAT_ID])
    data = [answer, datetime.datetime.now(), chat_id]
    cursor.execute(query, data)
    conn.commit()


def add_messages_id(chat_id, messages_id):
    for message_id in messages_id:
        query = insert_query(table_name=TABLE_MESSAGES_ID,
                             columns=[COLUMN_CHAT_ID, COLUMN_MI_MESSAGE_ID])
        data = [chat_id, message_id]
        cursor.execute(query, data)
    conn.commit()


def get_messages_id(chat_id):
    query = select_with_where_query(table_name=TABLE_MESSAGES_ID,
                                    select_columns=[COLUMN_MI_MESSAGE_ID],
                                    where_column=[COLUMN_CHAT_ID])
    data = [chat_id]
    record = cursor.execute(query, data)
    result = []
    for element in record:
        result.append(element[0])
    return result


def delete_messages_info(chat_id):
    query = delete_query(table_name=TABLE_MESSAGES_ID,
                         where_column=[COLUMN_CHAT_ID])
    data = [chat_id]
    cursor.execute(query, data)
    conn.commit()


def get_users_list():
    query = select_query(table_name=TABLE_USERS_INFO,
                         select_columns=[COLUMN_UI_USER_NAME, COLUMN_CHAT_ID])
    return cursor.execute(query)


def get_quiz_list():
    query = select_query(table_name=TABLE_QUIZ_SURPRISE_TYPE,
                         select_columns=[COLUMN_CHAT_ID, COLUMN_Q_PLAN, COLUMN_Q_WAIT, COLUMN_Q_EVENT,
                                         COLUMN_Q_TYPE, COLUMN_Q_COUNT, COLUMN_UPDATE_DATE, COLUMN_CREATION_DATE])
    return cursor.execute(query)
