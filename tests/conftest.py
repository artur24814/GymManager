import sqlite3
import os
import tempfile
from sql_question import CREATE_USERS_TABLE, CREATE_DAY_TABLE, CREATE_EX_TABLE, CREATE_STATS, CREATE_DAY_EXS
from models import User, Day, DayEx

import pytest

@pytest.fixture
def test_database():
    db_fd, db_path = tempfile.mkstemp()
    cnx = sqlite3.connect(db_path)
    cursor = cnx.cursor()
    cursor.execute(CREATE_USERS_TABLE)
    cursor.execute(CREATE_DAY_TABLE)
    cursor.execute(CREATE_EX_TABLE)
    cursor.execute(CREATE_DAY_EXS)
    cursor.execute(CREATE_STATS)
    cnx.commit()
    return cnx, cursor

@pytest.fixture
def user(test_database):
    cnx, cursor = test_database
    user = User(username='test', password='my_pass')
    user.create_user(cursor)
    cnx.commit()
    return user

@pytest.fixture
def day(test_database, user):
    cnx, cursor = test_database
    day = Day(user.username, 'day')
    day.create_day(cursor)
    cnx.commit()
    return day