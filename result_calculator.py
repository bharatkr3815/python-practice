# Write a Python program to create a Student Result Calculator.
# A beginner-friendly Python program that takes a student's name and marks in five subjects, 
# calculates the total marks and percentage, and assigns a grade based on the percentage. 
# The program also checks whether the student passes or fails based on the minimum marks requirement in each subject.


name = input('Enter your name :')

english = int(input('Enter your marks in English out of 100 :'))
maths = int(input('Enter your marks in Maths out of 100 :'))
science = int(input('Enter your marks in Science out of 100 :'))
s_science = int(input('Enter your marks in Social Science out of 100 :'))
hindi = int(input('Enter your marks in Hindi out of 100 :'))

total = english + maths + science + s_science + hindi
percentage = total/5


print('\n ==== Student Result ====')

print('Name :',name)
print('Total :',total)
print('Percentage :',percentage)

if english >= 33 and maths >= 33 and science >= 33 and s_science >= 33 and hindi >= 33:
    if percentage >= 90:
        print('Grade : A')
        print('Result : Pass')
    elif percentage >= 80:
        print('Grade : B')
        print('Result : Pass')
    elif percentage >= 70:
        print('Grade : C')
        print('Result : Pass')
    elif percentage >= 60:
        print('Grade : D')
        print('Result : Pass')
    elif percentage >= 50:
        print('Grade : E')
        print('Result : Pass')
    else:
        print('Grade : F')
        print('Result : Pass')
else:
    print('Result : Fail')