import sqlite3

from sql_question import CREATE_USERS_TABLE, CREATE_DAY_TABLE, CREATE_EX_TABLE, CREATE_STATS, CREATE_DAY_EXS


def create_connect():
    cnx = sqlite3.connect('gm.db')
    cursor = cnx.cursor()
    return cursor, cnx

cursor, cnx = create_connect()

cursor.execute(CREATE_USERS_TABLE)
cursor.execute(CREATE_DAY_TABLE)
cursor.execute(CREATE_EX_TABLE)
cursor.execute(CREATE_DAY_EXS)
cursor.execute(CREATE_STATS)
cnx.commit()
cnx.close()


