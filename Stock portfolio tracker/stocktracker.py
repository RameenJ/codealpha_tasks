import requests
import pandas as pd

# Your API key
ALPHA_VANTAGE_API_KEY = 'LO7ZWXRGURC6APUI'

def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    try:
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        stock_price = float(data['Time Series (1min)'][last_refreshed]['1. open'])
        return stock_price
    except KeyError:
        return None

portfolio = {}

def add_stock(symbol, quantity):
    price = get_stock_price(symbol)
    if price is not None:
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity
        print(f"Added {quantity} of {symbol} to portfolio.")
    else:
        print(f"Invalid stock symbol: {symbol}. Stock not added.")

def remove_stock(symbol, quantity):
    if symbol in portfolio:
        portfolio[symbol] -= quantity
        if portfolio[symbol] <= 0:
            del portfolio[symbol]
        print(f"Removed {quantity} of {symbol} from portfolio.")
    else:
        print(f"Stock symbol {symbol} not found in portfolio.")

def view_portfolio():
    portfolio_data = []
    for symbol, quantity in portfolio.items():
        price = get_stock_price(symbol)
        value = price * quantity if price else 0
        portfolio_data.append({'Symbol': symbol, 'Quantity': quantity, 'Price': price, 'Value': value})
    portfolio_df = pd.DataFrame(portfolio_data, columns=['Symbol', 'Quantity', 'Price', 'Value'])
    return portfolio_df

def get_portfolio_value():
    total_value = 0
    for symbol, quantity in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            total_value += price * quantity
    return total_value

def main():
    print("Welcome to the Stock Portfolio Tracker")
    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. View Portfolio Value")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio_df = view_portfolio()
            print(portfolio_df)
        elif choice == '4':
            total_value = get_portfolio_value()
            print(f"Total Portfolio Value: ${total_value:.2f}")
        elif choice == '5':
            print("Exiting the Stock Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
