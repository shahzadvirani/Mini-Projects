'''
Simple Calculator with four operations
(Add, Subtract, Multiply and Divide)
'''

#function definitions:
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

#prompt to users:
num1=float(raw_input("Enter first number: "))
num2=float(raw_input("Enter second number: "))

print("\t\t\t Select Operation:")
choice=int(raw_input("1.Addition 2.Subtraction 3.Multiplication 4.Division \n"))

while True:  #continuous loop to ensure that a valid option is chosen
    if (choice==1 or choice==2 or choice==3 or choice==4):
        break
    else:
        print("Please choose one of the above mentioned choices!")
        choice = int(raw_input("1.Addition 2.Subtraction 3.Multiplication 4.Division \n"))

if choice==1:
    answer=add(num1,num2)
elif choice==2:
    answer=subtract(num1,num2)
elif choice==3:
    answer=multiply(num1,num2)
else:
    answer=divide(num1,num2)

print("The answer is: " + str(answer))



