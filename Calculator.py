#Defining the things we can do:
#We will use def function here:
#Addition
def Addition():
  num1 = int(input("Enter Your First Number here:"))

  num2 = int(input("Enter Your Second number here:"))
  sum = (num1 + num2)
  print(f"{num1} + {num2} = {sum}")

#subtraction
def subtraction():
  num1 = int(input("Enter Your First Number here:"))

  num2 = int(input("Enter Your Second number here:"))
  sum = (num1 - num2)
  print(f"{num1} - {num2} = {sum}")

#multiplication
def multiplication():
  num1 = int(input("Enter Your First Number here:"))

  num2 = int(input("Enter Your Second number here:"))
  sum = (num1 * num2)
  print(f"{num1} * {num2} = {sum}")
#division
def division():
  num1 = int(input("Enter Your First Number here:"))

  num2 = int(input("Enter Your Second number here:"))
  sum = (num1 % num2)
  print(f"{num1} % {num2} = {sum}")

#Taking Command:
#Making a Loop

while True:
  Command = int(input(
    "Type '1' for addition \n Type '2' for subtraction \n Type '3' for multiplication \n Type '4' for division\n Type '5' for exit \n >  "))
#Command for Addition:
  if Command == 1:
    Addition()
#Command for Subtraction:
  elif Command == 2:
    subtraction()
#Command for Multiplication:
  elif Command == 3:
    multiplication()
#Command for Division:
  elif Command == 4:
    division()
#Breaking point and command for Exit:
  elif Command == 5:
    print("Thanks for your visit. BYE!")
    break