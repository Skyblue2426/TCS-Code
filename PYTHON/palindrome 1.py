def is_palindrome(num):
    num_str=str(num)
    if num_str==num_str[::-1]:
        return true
    else:
        return false
    x=int(input("enter a number"))
    if is_palindrome(x):
        print("palindrome number \n \n")
    else:
            print("not palindrome number  \n\n")
                  
