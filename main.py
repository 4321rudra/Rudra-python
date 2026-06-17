# hey= "Rudra"
# print(f" Hello {hey}")

# name =" Rudra"
# age=21.0
# is_student=True
# print(type(name))
# print(type(age))
# print(type(is_student))
# gps=int(age)
# # print(gps)
# name=input("What is your name : ")
# age=input("What is your agw ? : ")
# age=int(age)
# print(type(name))
# print(type(age))
# length=float(input("ENter l : "))
# b=float(input("ENter b : "))
# area =length*b
# print(area)

# company_name="KRBL"
# share_price=360.7
# shares_bought=10
# initial_investment=share_price*shares_bought
# after_event_price=share_price-share_price/10
# current_investment=after_event_price*shares_bought
# loss=initial_investment-current_investment
# if(loss>500):
#     print("Alert: Portfolio is down significantly! Consider a stop-loss.")
# elif(1<=loss<=500):
#     print("Minor market correction. Holding position.")
# else:
#     print("Portfolio is safe.")
# weekly_prices=[360.7, 352.1, 368.4, 341.0, 375.5]
# total_sum=0
# for p in weekly_prices:
#     total_sum+=p
#     if p<350:
#         print(f"Alert: Price dropped below support level: {p}")
# average=total_sum/5
# print(average)
# companies = [
#     {"name": "Company A", "ticker": "COMPA", "market_cap": 12000},
#     {"name": "Company B", "ticker": "COMPB", "market_cap": 3500},
#     {"name": "Company C", "ticker": "COMPC", "market_cap": 500}
# ]
# mid_large_count=0
# for c in companies:
#     if c["market_cap"]>5000:
#         print(f"Screened : {c["name"]} ({c["ticker"]}) qualifies")
#         mid_large_count+=1
# print(f"Total qualified companies found : {mid_large_count}")
dirty_portfolio = [
    {"ticker": "INFY", "price": "₹1,450.50"},
    {"ticker": "TCS", "price": "₹4,120.00"},
    {"ticker": "WIPRO", "price": "₹480.25"},
    {"ticker": "HCLTECH", "price": "₹1,320.10"}
]
total_value=0
for c in dirty_portfolio:
    c["price"]=float(c["price"].replace("₹", "").replace(",",""))
    total_value+=c["price"]
    print(f"Cleaned {c["ticker"]} : {c["price"]}")
average=round(total_value/4,2)
print(f"Portfolio average price : {average}")