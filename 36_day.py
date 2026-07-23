num =input("Enter the number:")
print(f"Multiplication of {num}:")
try:
          for i in range(1,11):
               print(f"{int(num)} x {i} = {int(num*i)}")
except Exception as E:
     print(E)

print("some line of code ")