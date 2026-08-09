unit = int(input('Enter units ='))

if unit>=0 and unit <=100:
    amount = unit * 5
elif unit>=101 and unit <=200:
    amount = unit * 7
else:
    amount = unit * 10

print('Total electricity bill = ',amount)