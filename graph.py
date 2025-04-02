import pandas as pd
import matplotlib.pyplot as plt
from logger import log_function

@log_function
def plot_stock_prices(file_path):
    stock_prices = pd.read_csv(file_path)
        
    plt.figure(figsize=(12, 6), dpi=100)
    up = stock_prices[stock_prices.Close >= stock_prices.Open]
    down = stock_prices[stock_prices.Close < stock_prices.Open]

    col_up = 'green'
    col_down = 'red'
    width = 0.6
    wick_width = 0.1
        
    plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col_up)
    plt.bar(up.index, up.High-up.Close, wick_width, bottom=up.Close, color=col_up)
    plt.bar(up.index, up.Low-up.Open, wick_width, bottom=up.Open, color=col_up)
        
    plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col_down)
    plt.bar(down.index, down.High-down.Open, wick_width, bottom=down.Open, color=col_down)
    plt.bar(down.index, down.Low-down.Close, wick_width, bottom=down.Close, color=col_down)
        
    plt.title(f'График акций Apple')
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.grid(True, linestyle='--', alpha=0.6)
        
    step = max(1, len(stock_prices) // 10)
    plt.xticks(
        ticks=range(0, len(stock_prices), step),
        labels=stock_prices['Date'].iloc[::step],
        rotation=45
    )
        
    plt.tight_layout()
    plt.show()
        