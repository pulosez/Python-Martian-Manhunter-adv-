import re
import os

if __name__ == "__main__":
    if os.path.exists('new_django_success.log'):
        os.remove('new_django_success.log')
    with open('django_success.log', 'r') as log_file:
        logfile = ''.join(log_file.readlines())
        logfile = re.sub(r'\[\d{2}\/\w{3}\/\d{4}\s(\d{2}:?){3}\]', '[XX/XXX/XXXX XX:XX:XX]', logfile)
        logfile = re.sub(r'[a-zA-Z0-9\-\_\/]*\/admin\/[a-zA-Z0-9\-\.\_\/]*', '/XXX/XXXXX/XXX', logfile)
        with open('new_django_success.log', 'a') as new_log_file:
            new_log_file.write(logfile)
