## simple calculator 

perform_operation= str(input("choose any operation"))
num1= float(input("enter first number"))
num2= float(input("enter second number"))


if perform_operation== "add":
    result= num1+ num2
elif perform_operation== "sub":
    result= num1-num2
elif perform_operation=="div":
    if num2!=0:
       result = num1/num2
    else: 
        result= "error" 
elif perform_operation=="multiply":
   result= num1*num2
elif perform_operation=="floordiv":
   result= num1//num2

else: 
   result= "invalid"   

print("result:", result)
