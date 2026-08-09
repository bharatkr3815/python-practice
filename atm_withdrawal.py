bal = int(input('Enter account balance ='))
amt = int(input('Enter withdrawal amount ='))

if amt <= bal:
    if amt % 100 == 0:
        print('Withdraw Successful')       
        remaining_amount = bal - amt
        print('Remaining Balance =',remaining_amount)
    else:
        print('Enter amount in multiples of 100')
else:
    print('Insufficient Balance')