city1_sales = 5000  
city1_cost = 3000   
city2_sales = 7000  
city2_cost = 4000   
city1_profit = city1_sales - city1_cost
city2_profit = city2_sales - city2_cost
if city1_profit > city2_profit:
    highest_profit_city = "City 1"
    difference = city1_profit - city2_profit
elif city2_profit > city1_profit:
    highest_profit_city = "City 2"
    difference = city2_profit - city1_profit
else:
    highest_profit_city = "Both cities have equal profit"
    difference = 0
print(f"Profit in City 1: ${city1_profit}")
print(f"Profit in City 2: ${city2_profit}")
if difference != 0:
    print(f"{highest_profit_city} has the highest profit.")
    print(f"Difference in profit: ${difference}")
else:
    print(f"Both cities have equal profit.")
