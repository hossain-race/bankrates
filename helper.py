# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License
# Helper Functions

import os
from datetime import datetime

# https verify issue solution
# https://bit.ly/2KKXIQD
def verify_https_issue():
    import os
    import ssl

    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context


def write_webpage_as_html(filename='html/temp.html', data=''):
    try:
        with open(filename, 'wb') as fobj:
            fobj.write(data)
    except Exception as e:
        print(e)
        return False
    else:
        return True


def read_webpage_from_html(filename='html/temp.html'):
    try:
        with open(filename) as fobj:
            data = fobj.read()
    except Exception as e:
        print(e)
        return False
    else:
        return data

def raw_data_filename(DIRS, command):
    return f'{DIRS["raw"]}{command}.html'

# Getting time difference in minutes when file last modified
def get_last_scraped_time(filename):
    if not os.path.exists(filename):
        return -1 # file doesn't exist

    file_time = os.path.getmtime(filename)
    now = datetime.timestamp(datetime.now())
    diff = now - file_time
    #print(file_time, now, diff)
    minutes = int(round(diff / 60))
    return minutes