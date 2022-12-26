from models import DayEx
import datetime

def test_create_day(test_database, user):
    cnx, cursor = test_database
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    day_result = DayEx(date, 600)
    day_result.create(cursor, cnx)
    cnx.commit()

    list_dayEx = DayEx.get_all(cursor)

    assert len(list_dayEx) == 1
    cnx.close()