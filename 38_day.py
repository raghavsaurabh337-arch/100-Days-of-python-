num=int(input("enter the value 5 or 20;"))
if num<5 or num>20:
    raise ValueError("Invalid input. Please enter a value between 5 and 20.")
