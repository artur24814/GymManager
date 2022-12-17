import sqlite3

CREATE_USERS_TABLE = """CREATE TABLE if not exists users(

    id INTEGER PRIMARY KEY, 

    username varchar(255) UNIQUE,

    hashed_password varchar(80))"""


CREATE_DAY_TABLE = '''CREATE TABLE if not exists days (
    id INTEGER PRIMARY KEY,
    user_name varchar(255) REFERENCES users(username) ON DELETE CASCADE,
    title varchar(355))
'''

CREATE_EX_TABLE = '''CREATE TABLE if not exists exercises (
    id INTEGER PRIMARY KEY,
    id_day INTEGER REFERENCES days(id) ON DELETE CASCADE,
    title varchar(255),
    weight INTEGER,
    repeat INTEGER)
'''
CREATE_DAY_EXS = '''CREATE TABLE if not exists day_exs (
    id INTEGER PRIMARY KEY NOT NULL,
    data varchar (200),
    time INTEGER)
    '''

CREATE_STATS = '''CREATE TABLE if not exists stats (
    id INTEGER PRIMARY KEY,
    days INTEGER,
    general_time INTEGER
)
'''
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


