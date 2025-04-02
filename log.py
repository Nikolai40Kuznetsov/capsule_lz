import getpass, os, sys, datetime, pandas as pd, matplotlib.pyplot as plt, csv
user_login = getpass.getuser()
print(user_login)
print (os.path.basename(sys.argv[0]))
current_date = datetime.datetime.now()
current_datetime = str(datetime.datetime.now()).split()
current_date = current_date.strftime('%d %m %Y')
current_time = current_datetime[1]
print(current_time)
print(current_date)
# инициируем датафрейм
data = [{"User_login": ['Test'], "Function_name": ['test_func'], "Date": current_date, "Time": current_time}]
df = pd.DataFrame(data)
df.loc[len(df)] = [user_login, None, current_date, current_time] 
# print(df)

with open('logs.csv', 'w', newline='') as csvfile:
    fieldnames = ["User_login", "Function_name", "Date", "Time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


stock_prices = pd.read_csv("AAPL.csv")
# print(stock_prices) 
plt.figure() 
up = stock_prices[stock_prices.Close >= stock_prices.Open] 
down = stock_prices[stock_prices.Close < stock_prices.Open] 
col1 = 'red' 
col2 = 'green' 
width = .3
width2 = .03
plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1) 
plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1) 
plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1) 
plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2) 
plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2) 
plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2) 
plt.xticks(rotation=30, ha='right') 
plt.show() 
# сделать оси цена и дата
# сделать декоратор
# нормализовать main.py
# сделать так, чтобы логи не перезаписывались, а писались все