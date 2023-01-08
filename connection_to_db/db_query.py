
INSERT_CHAT_ID_QUERY = 'INSERT INTO quiz_surprise_type (chat_id) VALUES (?);'
UPDATE_ANSWER_QUERY = 'Update quiz_surprise_type set q_type = ? where chat_id = ?'


def insert_query(table_name, columns):
    return 'INSERT INTO ' + table_name + ' ' + __create_brackets_list(columns) + \
           ' VALUES ' + __create_brackets_list_with_questions(len(columns)) + ';'


def insert_or_ignore_query(table_name, columns):
    return 'INSERT OR IGNORE INTO ' + table_name + ' ' + __create_brackets_list(columns) + \
           ' VALUES ' + __create_brackets_list_with_questions(len(columns)) + ';'


def update_query(table_name, columns, name_id_column):
    return 'UPDATE ' + table_name + ' SET ' + __create_equals_list(columns) + \
           ' WHERE ' + __create_equals_list(name_id_column) + ';'


def select_with_where_query(table_name, select_columns, where_column):
    return 'SELECT ' + __create_list(select_columns) + ' FROM ' + table_name + \
           ' WHERE ' + __create_equals_list(where_column) + ';'


def delete_query(table_name, where_column):
    return 'DELETE FROM ' + table_name + \
           ' WHERE ' + __create_equals_list(where_column) + ';'


def __create_brackets_list_with_questions(count):
    query = "("
    for i in range(count):
        query += "?, "
    return query[:-2] + ')'


def __create_brackets_list(elements):
    query = "("
    for element in elements:
        query += str(element) + ", "
    return query[:-2] + ')'


def __create_list(elements):
    query = ""
    for element in elements:
        query += str(element) + ", "
    return query[:-2]


def __create_equals_list(columns):
    query = ""
    for i in range(len(columns)):
        query += columns[i] + " = ?, "
    return query[:-2]
