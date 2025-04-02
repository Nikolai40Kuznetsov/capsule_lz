import getpass
import os
import datetime
import csv
from functools import wraps

def log_function(func):
    """Декоратор для логирования вызовов функций"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_login = getpass.getuser()
        script_name = os.path.basename(__file__)
        current_date = datetime.datetime.now().strftime('%d %m %Y')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        
        log_data = {
            "User_login": user_login,
            "Function_name": func.__name__,
            "Date": current_date,
            "Time": current_time
        }
        
        file_exists = os.path.isfile('logs.csv')
        with open('logs.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, 
                                fieldnames=["User_login", "Function_name", "Date", "Time"])
            if not file_exists:
                writer.writeheader()
            writer.writerow(log_data)
        
        return func(*args, **kwargs)
    return wrapper