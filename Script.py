hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Total Price
total_price = 0

for price in prices:
  total_price += price

print(total_price)

#Length of the list
total_price_length = len(prices)

#List Average
average_price = total_price/total_price_length
print(average_price)

#Comprehension List (price minus 5)
new_prices = [price - 5 for price in prices]
print(new_prices)

#Total Revenus
total_revenue = 0

#Foor loop
for i in range(len(hairstyles)):
  #We will code
  total_revenue += prices[i] * last_week[i]
  print("Total Revenue: ", total_revenue)

#Average number
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

#Comprehension
cuts_under_30 = []

print(cuts_under_30)
