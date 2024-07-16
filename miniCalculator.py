def add(x , y ) :
   return x+y 

def substract(x, y) :
   return x-y

def multiply (x, y) :
   return x * y

def divide(x, y) :
   #if y is 0 then return an error
   #else divide x with y 
    if y == 0:
       return "Error!!!! Division by 0."
    else:
       x/y


def calculator() :
  
   print("Simple Calculator")
   print("-------------------")
   print()
   print("Operations:")
   print("1. Add ")
   print("2. Subtract ")
   print("3. Multiply ")
   print("4. Divide ")
   print("5. Exit ")


## loop in while
while True :
# take input from user
   operation = input("Choose operation from 1 to 5: ")
# if the input is 5, break while loop 
   if operation == '5':
      print("Exiting simple Calculator")
      break

# list - items put together  ['1','2','3','4'] if choice in []
   if operation in ['1','2','3','4'] :
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      if operation == '1' :
        print(f"{num1} + {num2} = {add(num1, num2)}")
      elif operation == '2' :
        print(f"{num1} - {num2} = {substract(num1, num2)}")
      elif operation == '3' :
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
      elif operation == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
   #  if input invalid, give error message
   else :
      print ("Invalid Input.\n Enter anything from 1-5 ")
   


if __name__ == "__main__":
    calculator()
   