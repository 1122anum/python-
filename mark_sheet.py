# comparison operaters
marks = int (input("enter your marks : "))
if marks >= 90:
    grade = "A+"  
elif marks >=80 and  marks <= 90:
    grade = "A"
elif marks >= 70 and marks <= 80:
    grade = "B"
elif marks >= 60 and marks <= 70:
    grade = "C"
elif marks >= 50 and marks <= 60:
    grade = "D"
else:
    grade = "fail" 
print(("your grade is ->") , grade)
    
  

