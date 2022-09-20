num1=input("enter the first number")

if num1.isdigit():
   num1=int(num1)
   print("This program will perform all the following arithmetic operations: \n 1_ + \n 2_ - \n 3_ * \n 4_ / \n 5_ ^ \n 6_ %")
   num2= input("enter the second number")
   if num2.isdigit():
       num2 = int(num2)
       operation= input("enter the arithmetic operation you need from the above")
       if operation=='1' or operation=='+':
           output= num1+num2
           print(output)
       elif operation =='2' or operation=='-':
           output = num1-num2
           print(output)
       elif operation =='3' or operation=='*':
           output = num1*num2
           print(output)
       elif operation =='4' or operation == '/':
           output = num1/num2
           print(output)
       elif operation =='5' or operation == '^':
           output = num1^num2
           print(output)
       elif operation =='6' or operation == '%':
           output = num1%num2
           print(output)
       else:
           print("it is not a valid operation, please run the program again")
   else:
       print("it is not a number")
else:
   print("it is not a number")
print("The result is=",output)
print("please type the number of operation you would like to perform on the result:\n 1- round \n 2-ceiling \n 3-floor\n 4- convert the number into integer without the decimal point \n 5- stop")
option=input("enter the operation")
import math
if option=='1':
   output=round(output)
elif option=='2':
   output=math.ceil(output)
elif option == '3':
   output=math.floor(output)
elif option == '4':
   output= int(output)
elif option == '5':
   print("final output is=", output)
else:
   print("final output is=", output)
print("final output is=", output)

