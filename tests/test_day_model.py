from models import Day

def test_create_day(test_database, user):
    cnx, cursor = test_database
    day = Day(user.username, '1day')
    day.create_day(cursor)
    cnx.commit()

    list_days = Day.get_days_by_username(cursor, user.username)

    assert len(list_days) == 1
    cnx.close()

def test_delete_day(test_database, user, day):
    cnx, cursor = test_database
    day = Day(user.username, '2day')
    day.create_day(cursor)
    list_days = Day.get_days_by_username(cursor, user.username)

    assert len(list_days) == 2

    Day.delete_day(cursor, day.id)
    cnx.commit()
    list_days = Day.get_days_by_username(cursor, user.username)

    assert len(list_days) == 1

    cnx.close()