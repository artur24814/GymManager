from GMcrypto import hash_password


class User:
    def __init__(self, username='', password='', salt=''):
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password, salt)

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt=''):
        self._hashed_password = hash_password(password, salt)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)

    def create_user(self, cursor):
        if self._id == -1:
            sql = "INSERT INTO users (username, hashed_password) VALUES (?,?)"
            values = (str(self.username), str(self.hashed_password))
            cursor.execute(sql, values)
            self._id = cursor.lastrowid
            return True
        else:
            values = (self.username, self.hashed_password, self.id)
            sql = """UPDATE users SET username=?, hashed_password=?
                           WHERE id=?"""
            cursor.execute(sql, values)
            return True

    @staticmethod
    def get_user_by_id(cursor, id_):
        sql = 'SELECT id, username, hashed_password FROM users WHERE id=?'
        cursor.execute(sql, (id_,))
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None

    @staticmethod
    def load_user_by_username(cursor, username):
        sql = "SELECT id, username, hashed_password FROM users WHERE username=?"
        cursor.execute(sql, (username,))  # (username, ) - cause we need a tuple
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user

    def check_user(self, cursor):
        sql = 'SELECT id, username, hashed_password FROM users WHERE username=? AND hashed_password=?'
        value = (self.username, self.hashed_password)
        cursor.execute(sql, value)
        data = cursor.fetchone()
        if data:
            return True
        else:
            return None

    @staticmethod
    def get_all(cursor):
        sql = "SELECT id, username, hashed_password FROM users"
        users = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users

    def delete(self, cursor, id):
        sql = "DELETE FROM Users WHERE id=?"
        cursor.execute(sql, (id,))
        self._id = -1
        return True


class Day:
    def __init__(self, user_name, title):
        self._id = -1
        self.user_name = user_name
        self.title = title

    @property
    def id(self):
        return self._id

    def create_day(self, cursor):
        if self._id == -1:
            if User.load_user_by_username(cursor, self.user_name) is None:
                return None
            sql = '''INSERT INTO days (user_name, title)
                            VALUES(?, ?)'''
            values = (self.user_name, self.title)
            cursor.execute(sql, values)
            self._id = cursor.lastrowid
            return True
        else:
            return False

    @staticmethod
    def get_days_by_username(cursor, username):
        sql = 'SELECT id, user_name, title FROM days WHERE user_name=?'
        cursor.execute(sql, (username,))
        days = []
        for row in cursor.fetchall():
            id_, user_name, title = row
            loaded_item = Day(user_name, title)
            loaded_item._id = id_
            days.append(loaded_item)
        return days

    @staticmethod
    def get_day(cursor, id_day):
        sql = 'SELECT id, user_name, title FROM days WHERE id=?'
        cursor.execute(sql, (id_day, ))
        data = cursor.fetchone()
        if data:
            id, username, title = data
            loaded_day = Day(username, title)
            loaded_day._id = id
            return loaded_day

    @staticmethod
    def delete_day(cursor, id_day):
        sql = 'DELETE FROM days WHERE id=?'
        cursor.execute(sql, (id_day, ))


class EX:
    def __init__(self, id_day, title, weight, repeat):
        self._id = -1
        self.id_day = id_day
        self.title = title
        self.weight = weight
        self.repeat = repeat

    @property
    def id(self):
        return self._id

    def create_ex(self, cursor):
        if self._id == -1:
            if Day.get_day(cursor, self.id_day) is None:
                return None
            sql = "INSERT INTO exercises (id_day, title, weight, repeat) VALUES (?, ?, ?, ?)"
            values = (self.id_day, self.title, self.weight, self.repeat)
            cursor.execute(sql, values)
            self._id = cursor.lastrowid
            return True
        else:
            return False

    @staticmethod
    def get_ex(cursor, id_day):
        sql = "SELECT id, id_day, title, weight, repeat FROM exercises WHERE id_day=?"
        cursor.execute(sql, (id_day, ))
        exs = []
        for row in cursor.fetchall():
            id_, _id_day, title, weight, repeat = row
            loaded_ex = EX(_id_day, title, weight, repeat)
            loaded_ex._id = id_
            exs.append(loaded_ex)
        return exs

    @staticmethod
    def clean_ex(cursor, id_day):
        sql = f"DELETE FROM exercises WHERE id_day=?"
        cursor.execute(sql, (id_day, ))


class DayEx:

    def __init__(self, data, time):
        self._id = -1
        self.data = data
        self.time = time

    @property
    def id(self):
        return self._id

    def create(self, cursor, con):
        exists_day = DayEx.get_one(cursor, self.data)
        if exists_day:
            sql = 'UPDATE day_exs SET time=? WHERE data=?'
            new_time = exists_day.time + self.time
            cursor.execute(sql, (new_time, self.data))
            con.commit()
            days = len(DayEx.get_all(cursor))
            stats = Stats(days, self.time)
            stats.set_stats(cursor, con)
            print("##### DAY UPDATED #####")
            return True
        elif exists_day is None and self._id == -1:
            sql = '''INSERT INTO day_exs(data, time) VALUES (?,?)'''
            cursor.execute(sql, (self.data, self.time))
            con.commit()
            self._id = cursor.lastrowid
            days = len(DayEx.get_all(cursor))
            stats = Stats(days, self.time)
            stats.set_stats(cursor, con)
            print("&&&& DAY Created &&&&")
            return True
        else:
            return False

    @staticmethod
    def get_all(cursor):
        sql = 'SELECT id ,data, time FROM day_exs'
        cursor.execute(sql)
        list_day_ex = []
        for row in cursor.fetchall():
            id_, data, time = row
            loaded_day = DayEx(data, time)
            loaded_day._id = id_
            list_day_ex.append(loaded_day)
        return list_day_ex

    @staticmethod
    def get_one(cursor, day):
        sql = 'SELECT id, data, time FROM day_exs WHERE data=?'
        cursor.execute(sql, (day,))
        try:
            data = cursor.fetchone()
            if data:
                id_, data, time = data
                loaded_day = DayEx(data, time)
                loaded_day._id = id_
                return loaded_day
        except Exception:
            pass


class Stats:

    def __init__(self, days, general_time):
        self._id = -1
        self.days = days
        self.general_time = general_time

    @property
    def id(self):
        return self._id

    def set_stats(self, cursor, con):
        stat = Stats.get_stats(cursor)
        if stat is not None:
            sql = 'UPDATE stats SET days=?, general_time=? WHERE id=1'
            time = stat.general_time + self.general_time
            cursor.execute(sql, (self.days, time))
            con.commit()
            print("****STATS UPDATED****")
            return True

        elif stat is None and self._id == -1:
            sql = 'INSERT INTO stats (days, general_time) VALUES (?,?)'
            cursor.execute(sql, (self.days, self.general_time))
            con.commit()
            self._id = cursor.lastrowid
            print('$$$$ STATS CREATED $$$$')
            return True

    @staticmethod
    def get_stats(cursor):
        sql = 'SELECT * FROM stats'
        cursor.execute(sql)
        try:
            stat = cursor.fetchone()
            if stat:
                id_, days, general_time = stat
                loaded_stat = Stats(days, general_time)
                loaded_stat._id = id_
                return loaded_stat
        except Exception:
            pass


