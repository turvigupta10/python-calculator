## simple calculator 

perform_operation= str(input("choose any operation  from (+,-,/,//,*)"))
num1= float(input("enter first number"))
num2= float(input("enter second number"))


if perform_operation== '+':
    result= num1+ num2
elif perform_operation== '-':
    result= num1-num2
elif perform_operation=='/':
    if num2!=0:
       result = num1/num2
    else: 
        result= "error" 
elif perform_operation=='*':
   result= num1*num2
elif perform_operation=='//':
   result= num1//num2

else: 
   result= "invalid"   

print("result:", result)
