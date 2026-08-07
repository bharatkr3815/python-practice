# Python program that asks the user to enter a username and a password

username = 'admin'
password = '1234'

name = input('Enter username =')
passs = input('Enter password =')

if name == username and passs == password:
    print('Login Successful')
else:
    print('Invalid username or password')