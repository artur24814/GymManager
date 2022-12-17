from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget, MDList, OneLineIconListItem, \
    OneLineAvatarIconListItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.datatables import MDDataTable

from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp

from models import User, Day, EX, DayEx
from conn_sqllite import create_connect

import csv
import datetime



def get_username():
    try:
        with open('session.cvs', newline='') as session:
            reader = csv.DictReader(session)
            for row in reader:
                username = row['username']
        return username
    except Exception:
        return ''


class RegisterWindow(MDScreen):
    def create_user(self, login, password):
        print(login, password)
        user = User(username=login, password=password)
        cursor, cnx = create_connect()
        user.create_user(cursor)
        print(user)
        cnx.commit()
        cnx.close()
        self.manager.current = 'login'


class LoginWindow(MDScreen):
    def check_user(self, login, password):
        user = User(username=login, password=password)
        cursor, cnx = create_connect()
        login = user.check_user(cursor)
        cnx.close()
        if login is True:
            self.manager.current = 'list'
            with open('session.cvs', mode='w', newline='') as session:
                fieldnames = ['username', 'login']
                writer = csv.DictWriter(session, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'username': user.username, 'login': True})
        # else:
        #     self.add_widget(Label(text='Error'))

class MyListItemButton(OneLineAvatarIconListItem):
    def on_press(self, *args, **kwargs):
        app = MDApp.get_running_app()
        app.root.get_screen('day-detail').create_content(self.id)
        super().on_press()


class IconForDelete(IconRightWidget):
    pass


class ListWindow(MDScreen):
    pass

class DayView(MDList):
    def __init__(self, *args, **kwargs):
        super(DayView, self).__init__(*args, **kwargs)
        self.create_list_days()
        self.username = get_username()

    def create_list_days(self):
        cursor, cnx = create_connect()
        username = get_username()
        list_days = Day.get_days_by_username(cursor, username)
        if list_days is None:
            return False
        for item in list_days:
            button = MyListItemButton()
            icon = IconLeftWidget()
            icon_right = IconForDelete()
            icon.icon = 'weight-lifter'
            icon_right.icon = 'minus'
            icon_right.id = str(item.id)
            button.text = f"{item.title}"
            button.id = str(item.id)
            button.add_widget(icon)
            button.add_widget(icon_right)
            self.add_widget(button)
        cnx.commit()
        cnx.close()

    def create_new_day(self, day):
        print(self.username)
        if day == '':
            return False
        day = Day(self.username, day)
        cursor, cnx = create_connect()
        day.create_day(cursor)
        cnx.commit()
        cnx.close()
        self.clear_widgets()
        self.create_list_days()

    def delete_one_day(self, id_day):
        cursor, cnx = create_connect()
        Day.delete_day(cursor, id_day)
        cnx.commit()
        cnx.close()
        self.clear_widgets()
        self.create_list_days()


class DayDetailView(MDScreen):

    def __init__(self, *args, **kwargs):
        super(DayDetailView, self).__init__(*args, **kwargs)
        self.id_day = ''

    def save_day(self, name1, weight1, repeat1, name2, weight2, repeat2, name3, weight3, repeat3, name4, weight4,
                 repeat4, name5, weight5, repeat5, name6, weight6, repeat6):
        for i in range(1, 7):
            if locals()[f'name{i}'] == '':
                exec('self.ids.name' + str(i) + '.text = "Cant be blank"')
                return False
            if locals()[f'weight{i}'] == '':
                exec('self.ids.weight' + str(i) + '.text = "Cant be blank"')
                return False
            if locals()[f'repeat{i}'] == '':
                exec('self.ids.repiat' + str(i) + '.text = "Cant be blank"')
                return False
        cursor, cnx = create_connect()
        exs = EX.get_ex(cursor, self.id_day)
        if len(exs) != 0:
            EX.clean_ex(cursor, self.id_day)
        for i in range(1, 7):
            name = locals()[f'name{i}']
            weight = locals()[f'weight{i}']
            repeat = locals()[f'repeat{i}']
            ex = EX(self.id_day, name, weight, repeat)
            ex.create_ex(cursor)
            print('ok')
        cnx.commit()
        cnx.close()

    def create_content(self, id_day):
        cursor, cnx = create_connect()
        self.id_day = id_day
        day = Day.get_day(cursor, id_day)
        exs = EX.get_ex(cursor, id_day)
        self.ids.toolbar.title = day.title
        if len(exs) != 0:
            for i in range(6):
                exec('self.ids.name' + str(i+1) + '.text = exs[' + str(i) + '].title')
                exec('self.ids.weight' + str(i+1) + '.text = str(exs[' + str(i) + '].weight)')
                exec('self.ids.repiat' + str(i+1) + '.text = str(exs[' + str(i) + '].repeat)')
        else:
            for i in range(6):
                exec('self.ids.name' + str(i+1) + '.text = ""')
                exec('self.ids.weight' + str(i+1) + '.text = ""')
                exec('self.ids.repiat' + str(i+1) + '.text = ""')
        cnx.close()
        app = MDApp.get_running_app()
        app.root.current = 'day-detail'

class Tables(MDScreen):

    def __init__(self, **kwargs):
        super(Tables, self).__init__(**kwargs)
        self.table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = True,
            use_pagination = True,
            column_data=[
                ('id', dp(self.width/3)),
                ('Date', dp(self.width/3)),
                ('Time', dp(self.width/3)),
            ],
            row_data = [
                (1, '12/10/2022', 21.3),
                (2, '12/10/2022', 21.3),
                (3, '12/10/2022', 21.3),
                (1, '12/10/2022', 21.3),
                (2, '12/10/2022', 21.3),
                (3, '12/10/2022', 21.3),
                (1, '12/10/2022', 21.3),
                (2, '12/10/2022', 21.3),
                (3, '12/10/2022', 21.3),
                (1, '12/10/2022', 21.3),
                (2, '12/10/2022', 21.3),
                (3, '12/10/2022', 21.3),
            ]
        )
        self.table.bind(on_check_press=self.checked)
        self.table.bind(on_row_press=self.row_checked)
        self.add_widget(self.table)

    def checked(self, instance_table, current_row):
        print(current_row)

    def row_checked(self, instance_table, instance_row):
        print(instance_row)


class TimerLayout(RelativeLayout):
    minutes = NumericProperty()
    global_time = NumericProperty()

    def __init__(self, **kwargs):
        super(TimerLayout, self).__init__(**kwargs)
        self.minutes = 0
        self.general_time = 0
        self.time = 0
        #counter
        self.global_time = 0

    def increment_time(self, dt):
        self.ids.time_elipse.canvas.after.get_group('a')[0].angle_end += .6
        self.time = round(self.time + .1, 1)
        self.general_time = round(self.general_time + .1, 1)
        if self.time > 60:
            self.minutes = int(self.general_time / 60)
            self.time = 0
        self.ids.time_sec.text = str(self.time)

    def increment_time_global(self, dt):
        self.global_time += 1
        if self.global_time < 10:
            self.ids.counter.text = '00.00.0' + str(self.global_time)
        elif 10 <=self.global_time < 60:
            self.ids.counter.text = '00.00.' + str(self.global_time)
        elif self.global_time >= 60:
            minutes = int(self.global_time / 60)
            hours = int(self.global_time / 3600)
            if minutes > 59:
                minutes = minutes % 60
            if minutes < 10:
                minutes = '0' + str(minutes)
            sec = self.global_time % 60
            if sec < 10:
                sec = '0' + str(sec)
            if hours < 10:
                hours = '0' + str(hours)
            if int(hours) > 24:
                self.stop_count()
            self.ids.counter.text = str(hours) + '.' + str(minutes) + '.' + str(sec)

    # To start the count
    def start(self):
        # Clock.unschedule(self.increment_time)
        self.ids.stop_btn.disabled = False
        self.ids.start_btn.disabled = True
        self.ids.reset_btn.disabled = True
        Clock.schedule_interval(self.increment_time, .1)

    # To stop the count / time
    def stop(self):
        Clock.unschedule(self.increment_time)
        self.ids.stop_btn.disabled = True
        self.ids.start_btn.disabled = False
        self.ids.reset_btn.disabled = False

    def reset(self):
        self.ids.time_elipse.canvas.after.get_group('a')[0].angle_end = 0
        self.time = 0
        self.general_time = 0
        self.ids.time_sec.text = str(self.time)
        self.ids.reset_btn.disabled = True
        self.minutes = 0

    def start_count(self):
        Clock.schedule_interval(self.increment_time_global, 1)
        self.ids.counter_stop_btn.disabled = False
        self.ids.counter_start_btn.disabled = True
        self.ids.counter_save_btn.disabled = True

    def save_count(self):
        cursor, conn = create_connect()
        data = datetime.datetime.now().strftime('%Y-%m-%d')
        day_result = DayEx(data, self.global_time)
        day_result.create(cursor, conn)
        conn.close()
        self.global_time = 0
        self.ids.counter.text = '00.00.0' + str(self.global_time)
        self.ids.counter_stop_btn.disabled = True
        self.ids.counter_start_btn.disabled = False
        self.ids.counter_save_btn.disabled = True

    def stop_count(self):
        Clock.unschedule(self.increment_time_global)
        self.ids.counter_start_btn.disabled = False
        self.ids.counter_stop_btn.disabled = True
        self.ids.counter_save_btn.disabled = False


class GimManagerApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Indigo'
        sm = MDScreenManager()
        try:
            with open('session.cvs', newline='') as session:
                reader = csv.DictReader(session)
                for row in reader:
                    if row['login'] == 'True':
                        print(f"user {row['username']}login")
                        sm.add_widget(ListWindow(name='list'))
                        sm.add_widget(DayDetailView(name='day-detail'))
                        sm.add_widget(Tables(name='tables'))
                        return sm
        except Exception:
            sm.add_widget(LoginWindow(name='login'))
            sm.add_widget(RegisterWindow(name='register'))
            sm.add_widget(ListWindow(name='list'))
            sm.add_widget(DayDetailView(name='day-detail'))
            sm.add_widget(Tables(name='tables'))
            return sm

    def get_username(self):
        username = get_username()
        return username


if __name__ == '__main__':
    GimManagerApp().run()