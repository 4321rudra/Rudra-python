portfolio_1 = [
    {"ticker": "TATASTEEL", "price": 165.50, "shares": 50},
    {"ticker": "RELIANCE", "price": 2450.00, "shares": 10},
    {"ticker": "ITC", "price": 430.20, "shares": 100}
]

portfolio_2 = [
    {"ticker": "ZOMATO", "price": 185.00, "shares": 200},
    {"ticker": "MRF", "price": 125000.00, "shares": 1}
]
def analyze_stocks(portfolio_list):
    total_value=0
    for p in portfolio_list:
        total_value+=p["price"]*p["shares"]
    return total_value


total_value=analyze_stocks(portfolio_1)
print(f"Total value of portfolio 1 : {total_value}")
total_value=analyze_stocks(portfolio_2)
print(f"Total value of portfolio 2 : {total_value}")


