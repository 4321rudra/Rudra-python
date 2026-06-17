# import numpy as np
# # Copy this into your code
# closing_prices = [360.7, 352.1, 368.4, 341.0, 375.5]
# prices_array=np.array(closing_prices)
# adjusted_prices=prices_array-5.50
# print(adjusted_prices)
# print(np.max(adjusted_prices))
# print(min(adjusted_prices))
# Problem a
# def tt_sum_positive(amounts):
#     total_sum=0
#     for a in amounts:
#         if  isinstance(a,(int,float))  and a>0 :
#             total_sum+=a
#     return total_sum
# tr_am=[1200, -500, 3400, 0, "2300", 4500, None]
# total_sum=tt_sum_positive(tr_am)
# print(f"Total sum : {total_sum}")
# IDs=[101, 102, 103, 101, 104, 102, 105]
# dublicate =[]
# for i in IDs:
#     count=0
#     for j in IDs:
#         if i==j  :
#             count+=1
#     if(count>1 and i not in dublicate):
#         dublicate.append(i)
# print(dublicate)

stocks = [
    {"name": "Stock A", "allocation": 40, "risk": "High"},
    {"name": "Stock B", "allocation": 20, "risk": "Low"},
    {"name": "Stock C", "allocation": 40, "risk": "Medium"}
]
for i in stocks:
    if (i["risk"]=="Low" or i["risk"]=="Medium") and i["allocation"]==40:
        print(f"Name : {i["name"]}")