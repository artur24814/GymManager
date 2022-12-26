from models import EX

def test_create_exercise(test_database, user, day):
    cnx, cursor = test_database
    ex = EX(day.id, 'test', '20', '8')
    create = ex.create_ex(cursor)
    cnx.commit()

    assert create is True

    list_all_ex = EX.get_ex(cursor, id_day=day.id)

    assert len(list_all_ex) == 1
    cnx.close()


def test_clean_exercises(test_database, user, day):
    cnx, cursor = test_database
    for i in range(1, 7):
        ex = EX(day.id, f'test{i}', '30', '10')
        ex.create_ex(cursor)
        cnx.commit()

    list_all_ex = EX.get_ex(cursor, id_day=day.id)

    assert len(list_all_ex) == 6

    EX.clean_ex(cursor, day.id)

    list_new_ex = EX.get_ex(cursor, id_day=day.id)

    assert len(list_new_ex) == 0
