def is_valid_password(password):
   
    has_upper = False
    has_lower = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"

 
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char .isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

   
    return has_upper and has_lower and has_digit and has_special

password = input("Enter your lover  password : ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
