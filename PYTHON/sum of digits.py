def sum_of_divisible_digits(n):
    if n == 0:
        return 0  
    total_sum = 0 
    for digit in str(abs(n)):  
        d = int(digit)
        if d != 0 and n % d == 0: 
            total_sum += d
    return total_sum
number = 126
result = sum_of_divisible_digits(number)
print(f"The sum of the digits of {number} that divide {number} is {result}")
