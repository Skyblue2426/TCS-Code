def generate_change_table(bill_amount, customer_given):
    balance = customer_given - bill_amount
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    change_table = []
    for denom in denominations:
        count = balance // denom
        balance %= denom
        change_table.append([denom, count,])
    return change_table
bill = 262
customer_payment = 500
change_table = generate_change_table(bill, customer_payment)
print("Bill Amount:", bill)
print("Customer Given:", customer_payment)
print("Balance:", customer_payment - bill)
print("Possible Ways:")
print("Denomination | Count")
for row in change_table:
    print(f"{row[0]:^10} | {row[1]:^5}")
