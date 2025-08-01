#basic calculator program

first_number = int(input("Enter a first number : "))

print("1 - Add")
print("2 - Subtract")
print("3 - Multiple")
print("4 - Divide")

option = int(input("choose an operation : "))

second_number = int(input("enter a second number : "))

if option == 1:
    result = first_number + second_number
    print(f"the result is {result}") 

elif option == 2:
    result = first_number - second_number
    print(f"the result is {result}") 

elif option == 3:
    result = first_number * second_number
    print(f"the result is {result}") 

elif option == 4:
    result = first_number / second_number
    print(f"the result is {result}") 

else:
    print(f"Invalid Operation  \nChoose one option")

 
  