import sys
import logger as l
from graph import plot_stock_prices

if __name__ == "__main__":
    file_path = "AAPL.csv"
    plot_stock_prices(file_path)
