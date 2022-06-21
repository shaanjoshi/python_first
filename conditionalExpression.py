# 1. if-elif-else ladder in Python

a = 8
'''
if(a<3): 
    print("The value of a is greater than 3")
elif(a>13):
    print("The value of a is greater than 13")
elif(a>7):
    print("The value of a is greater than 7")
elif(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("done")    
'''

# 2. Multiple if statements
'''
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("Done")
'''

#Quick Quiz
'''
age = int(input("Enter the age: "))

if (age>=18):
    print("yess")
else:
    print("No")    
'''

#in and is operator
''''
a = None
if (a is None):
    print("Yes")
else:
    print("No")
'''
#****
'''
a = [45, 56, 6]
print(435 in a)
'''

#problem 1 (greatest number program)
'''
num1 = float(input("Enter a 1st number: "))
num2 = float(input("Enter a 2nd number: "))
num3 = float(input("Enter a 3rd number: "))
num4 = float(input("Enter a 4th number: "))

if(num1>num2):
    f1 = num1
else:
    f1 = num2
if(num3>num4):
    f2 = num3
else:
    f2 = num4
if(f1>f2):
    print(str(f1) + " is greatest among entered number")
else:
    print(str(f2) + " is greatest among entered number")
'''
#problem 2 (Result telling program)
'''
m1 = float(input("Enter Mathematics marks: "))
m2 = float(input("Enter Science marks: "))
m3 = float(input("Enter Hindi marks: "))
m4 = float(input("Enter English marks: "))

avg = m1 + m2 + m3 + m4 / 4

if(m1<33 or m2<33 or m3<33 or m4<33):
    print("You're fail because you have less than 33% in any of subject")
elif(avg<40):
    print("You're fail because avg is less than 40 %")
else:
    print("You are pass")
'''
#problem 3 (spam comment program)
'''
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
'''
#Problem 4 (Find wether given username have less than 10 character or not)
'''
uName = input("Enter the username: ")

lengthOfuName = len(uName)
print("Length of name is " + str(lengthOfuName))

if(lengthOfuName>10):
    print("username should not have more than 10 character")
else:
    print("username accepted")
'''
#problem 5 (Find whether given name is present in the list or not)
'''
listOfStudent = ["shaan", "rakesh", "ram", "shaam" ,"ritu"]

usrInput = input("Enter the name to check wether it's in list or not: ")

if(usrInput in listOfStudent):
    print("Congratulation you have qualified this round")
else:
    print("Better luck next time")
'''
#problem 6 (Grading system)
'''
marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)
'''