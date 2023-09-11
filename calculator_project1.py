#code soft internship
#task 1.
#design a simple calculator with basic arithmetic operations. prompt the user to input two numbers and an operation
#choice perform the calculation and display the result
a=int(input("enter first number:\n"))
b=int(input("enter seconf number:\n"))
operator=input("enter the operator(+,-,*,/,%):\n")
if(operator=='+'):
    print("the sum is:",a+b)
elif(operator=='-'):
    print("the subtraction is :",a-b)
elif(operator=='*'):
    print("the multiplication is :",a*b)
elif(operator=='/'):
    print("the division is :",a/b)
elif(operator=='%'):
    print("the modulo is :",a%b)
else:
    print("you entered wrong operator!!!")
print("Thank you!!!")