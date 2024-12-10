def is_palindrome(n):
    return str(n) == str(n)[::-1]
palindromes = []
for num in range(1, 15000):
    if is_palindrome(num):
        palindromes.append(num)
print(palindromes)
