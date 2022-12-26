from models import User

def test_create_user(test_database):
    cnx, cursor = test_database
    user = User(username='a', password='pass')
    created = user.create_user(cursor)
    cnx.commit()

    assert created is True
    check_user = User.load_user_by_username(cursor,'a')

    assert check_user is not None
    cnx.close()

def test_check_user(test_database, user):
    cnx, cursor = test_database
    user = User(username='test', password='my_pass')
    login = user.check_user(cursor)
    cnx.commit()

    assert login is True
    cnx.close()

def test_delete_user(test_database, user):
    cnx, cursor = test_database
    user = User(username='a2', password='password')
    created = user.create_user(cursor)
    cnx.commit()

    assert created is True
    deleted = user.delete(cursor, user.id)
    cnx.commit()

    assert deleted is True

    all_users = len(User.get_all(cursor))

    assert all_users == 1
    cnx.close()

