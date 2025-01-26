num1 = int (input("enter your first value : "))
num2 = int (input("enter your second value : "))
num3 = int (input("enter your third value : ")) 
num4 = int (input("enter your forth value : "))
if(num1 >= num2 and num2 <= num1):
    print("greatest number is" , num1)
elif( num2 >= num3 and num3 <= num2):
    print("greatest number is" , num2)
elif(num3 >= num4 and num4 <= num3 ):
    print("greatest number is", num3)
else:
    print("greatest number is", num4)
    
