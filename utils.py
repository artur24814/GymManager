import csv

def get_username():
    """
    Get username from session
    :return: string 'username'
    """
    try:
        with open('session.cvs', newline='') as session:
            reader = csv.DictReader(session)
            for row in reader:
                username = row['username']
        return username
    except Exception:
        return ''

def counter_time(time):
    '''
    Conventor sec to Hours:min:sec
    :param time: integer
    :return: string Hours:min:sec
    '''
    minutes = int(time / 60)
    hours = int(time / 3600)
    if minutes > 59:
        minutes = minutes % 60
    if minutes < 10:
        minutes = '0' + str(minutes)
    sec = time % 60
    if sec < 10:
        sec = '0' + str(sec)
    if hours < 10:
        hours = '0' + str(hours)
    return str(hours) + '.' + str(minutes) + '.' + str(sec)