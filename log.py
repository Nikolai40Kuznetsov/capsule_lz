import getpass
import os
import sys
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import csv
from functools import wraps

# Декоратор для логирования
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Логирование перед выполнением функции
        user_login = getpass.getuser()
        script_name = os.path.basename(sys.argv[0])
        current_date = datetime.datetime.now().strftime('%d %m %Y')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        
        log_data = {
            "User_login": user_login,
            "Function_name": func.__name__,
            "Date": current_date,
            "Time": current_time
        }
        
        # Запись в CSV 
        file_exists = os.path.isfile('logs.csv')
        with open('logs.csv', 'a', newline='') as csvfile:
            fieldnames = ["User_login", "Function_name", "Date", "Time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            writer.writerow(log_data)
        
        # Выполнение функции
        return func(*args, **kwargs)
    return wrapper

# Применяем декоратор к функции построения графика
@log_function
def plot_stock_prices(file_path):
    stock_prices = pd.read_csv(file_path)
    
    plt.figure(figsize=(12, 6)) 
    up = stock_prices[stock_prices.Close >= stock_prices.Open] 
    down = stock_prices[stock_prices.Close < stock_prices.Open] 
    
    col1 = 'green'  # Зеленый для роста цены
    col2 = 'red'    # Красный для падения цены
    width = 0.6
    width2 = 0.1
    
    # Рисуем свечи для роста
    plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1) 
    plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1) 
    plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1) 
    
    # Рисуем свечи для падения
    plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2) 
    plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2) 
    plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2) 
    
    # Настройка осей и заголовка
    plt.title('График свечей AAPL')
    plt.xlabel('Дата')
    plt.ylabel('Цена ($)')
    
    # Форматирование оси X (даты)
    plt.xticks(
        ticks=range(0, len(stock_prices), len(stock_prices)//10),
        labels=stock_prices['Date'].iloc[::len(stock_prices)//10],
        rotation=45
    )
    
    plt.tight_layout()
    plt.show()

# Вызов функции с построением графика
if __name__ == "__main__":
    plot_stock_prices("AAPL.csv")