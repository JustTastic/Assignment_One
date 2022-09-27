# Question 1
from imaplib import Int2AP


print("Question 1")
x = 101
y = 0
z = 0
if x > 100:
    y = 20
    z = 40
    print(f"Y is: {y} and Z is: {z}")

# Question 2
print("Question 2")
a = 100
b = 0 
c = 0
if a == 100:
    b = 10
    c = 50
    print(f"B is: {b} and C is: {c}")

# Question 3
print("Question 3")
a = 11
b = 0
if a < 10:
    b = 0
    print(f"B is: {b}")
else:
    b = 99
    print(f"B is: {b}")

# Question 4
print("Question 4")
score = 89
a_score = 90
b_score = 80
c_score = 70
d_score = 60
if score >= a_score:
    print("Your Score Is A")
elif score >= b_score:
    print("Your Score Is B")
elif score >= c_score:
    print("Your Score Is C")
elif score >= d_score:
    print("Your Score Is D")
else:
    print("Your Grade Is F")

# Question 5
print("Question 5")
num = int(input("Enter a number: "))
if num == 0:
    print("Your Number is Zero")
elif num > 0:
    print("Your Number Is positive")
    if num % 2 == 0:
        print("Your Number Is Even And")
    elif num % 2 != 0:
        print("Your Number Is Odd")
elif num < 0:
    print("Your Number Is negative")
else:
    print("Your Number Doesn't Exist")

# Question 6
print("Question 6")
len, wid = (input("Length And Width of rectangle 1: ")).split()
len2, wid2 = input("Length And Width of rectangle 2: ").split()

if int(len) * int(wid) > int(len2) * int(wid2):
    print("Rectangle 1 Has a Bigger Area")
else:
    print("Rectangle 2 Has a Bigger Area")

# Question 7
print("Question 7")
month_number = int(input("Enter A month In A Numeric Form: "))
if month_number == 1:
    print("First Quarter")
elif month_number == 2:
    print("First Quarter")
elif month_number == 3:
    print("First Quarter")
elif month_number == 4:
    print("Second Quarter")
elif month_number == 5:
    print("Second Quarter")
elif month_number == 6:
    print("Second Quarter")
elif month_number == 7:
    print("Third Quarter")
elif month_number == 8:
    print("Third Quarter")
elif month_number == 9:
    print("Third Quarter")
elif month_number == 10:
    print("Fourth Quarter")
elif month_number == 11:
    print("Fourth Quarter")
elif month_number == 12:
    print("Fourth Quarter")
else:
    print("INVALID MONTH Number")

# Question 8
print("Question 8")
num = int(input("Enter A number: "))
if num == 1:
    print("I")
elif num == 2:
    print("II")
elif num == 3:
    print("III")
elif num == 4:
    print("IV")
elif num == 5:
    print("V")
elif num == 6:
    print("VI")
elif num == 7:
    print("VII")
elif num == 8:
    print("VIII")
elif num == 9:
    print("IX")
elif num == 10:
    print("X")
else:
    print("Dont Know Roman numeric of this number")

# Question 9
print("Question 9")
f_test, s_test, exam = int(input("Enter Your First Test, Second Test and Exam: ")).split()


# Question 10
print("Question 10")

