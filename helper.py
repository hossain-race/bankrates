# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License
# Helper Functions

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