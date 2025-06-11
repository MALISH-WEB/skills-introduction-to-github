print("Welcome to Number Teller!")
number = int(input("please enter a number between 1 and 9"))
if number == 1:
    print("you have entered Number one")
elif number == 2:
    print("you have entered Number two")
elif number == 3:
    print("you have entered Number three")
elif number == 4:
    print("you have entered Number four")
elif number == 5:
    print("you have entered Number five")
elif number == 6:
    print("you have entered Number six")
elif number == 7:
    print("you ahve printed Number seven")
elif number == 8:
    print("you have entered Number eight")
elif number == 9:
    print("you have entered Number nine")
else:
    print("Invalid, please enter a number between 1 and 9")

#TODO
'''
With the use of If statement, write a python program that allows instructor to enter a mark strickly between 0 and 100.

on recieing the mark, the program has to assign a grade baesd on your defined clusters ie 80-90 is A, 91-100 is A+ etc.
'''


print("Welcome to UCU Grading Scale")
marks = int(input("please enter marks between 0 and 100"))
if marks >= 91 and marks <= 100:
   print("A+")
elif marks >= 81 and marks <=90:
    print("A")
elif marks >= 71 and marks <= 80:
    print("B+")
elif marks >= 61 and marks <= 70:
    print("B+")
elif marks >= 51 and marks <= 60:
    print("C+")
elif marks >=41 and marks <= 50:
    print("C")
elif marks >= 31 and marks <=40:
    print("D+")
elif marks >=21 and marks <=30:
    print("D")
elif  marks >=11 and marks <=20:
    print("E")
elif marks >=0 and marks <=10:
    print("fail")
else:
    print("Invalid, please enter a mark between 0 and 100")
