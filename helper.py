# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# Helper Functions

# https verify issue solution
# https://bit.ly/2KKXIQD
def verify_https_issue():
    import os, ssl
    
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
        ssl._create_default_https_context =             ssl._create_unverified_context