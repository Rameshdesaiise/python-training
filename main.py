import os
import datetime


def depositcash():
    deposit_amount = float(input('Please enter amount to be deposited:'))
    username = input('Please enter CardNum:')
    filename = username + '.txt'
    transactionfilename = '_transactionhistory.txt'
    transactionfile = open(transactionfilename, 'a')
    file = open(filename, 'a')
    balance = 0
    new_balance = 0
    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open(filename, 'w+') as file2:
        new_balance = balance + deposit_amount
        new_balance = str(new_balance)
        file2.write(new_balance)
        print('Your new balance is:', new_balance)
    with open(transactionfilename, 'a') as file3:
        balance = str(balance)
        deposit_amount = str(deposit_amount)
        file3.write(str(datetime.datetime.now()))
        file3.write(
            '\nPrevious balance: ' + balance + '. Deposit amount is:' + deposit_amount + '. New balance:' + new_balance + '\n')

    file.close()


def withdrawalcash():
    withdrawn_amount = float(input('Please enter amount to be withdrawn:'))
    username = input('Please enter CardNum:')
    filename = username + '.txt'
    transactionfilename =  '_transactionhistory.txt'
    transactionfile = open(transactionfilename, 'a')
    file = open(filename, 'a')
    balance = 0
    new_balance = 0

    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open(filename, 'w+') as file2:
        if withdrawn_amount > balance:
            print('You have insufficient balance. Your balance is:', balance)


        else:
            new_balance = balance - withdrawn_amount
            new_balance = str(new_balance)
            file2.write(new_balance)
            print('Your new balance is:', new_balance)
            with open(transactionfilename, 'a') as file3:
                balance = str(balance)
                withdrawn_amount = str(withdrawn_amount)
                file3.write(str(datetime.datetime.now()))
                file3.write(
                    '\nPrevious balance: ' + balance + '. Withdrawn amount is:' + withdrawn_amount + '. New balance:' + new_balance + '\n')
    file.close()


def balance():
    username = input('Please enter username:')
    filename = username + '.txt'
    file = open(filename, 'a')
    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
        file.seek(0)
        if file.read(1):
            print ('Your balance is:', balance)

        else:
            print('You have no balance left.')
    file.close()

def pinChange():
    cardNumber = input("Enter the Card Number:")
    cust_profile = open('cust_profile.txt', 'r')
    data = cust_profile.readlines()
    if cardNumber in data[0]:
        pin = input("Enter the OTP(eg 6789):")

        if(pin == "6789" ):
            newPin = input("Enter the new pin: ")
            data[1] = "pin : "+ newPin
            cust_profile.open('cust_profile', 'w+')
            cust_profile.writelines(data)
            cust_profile.close()

print('Hello ! Welcome to my bank !')
print('Please login to proceed.')

cust_profile = open('cust_profile.txt', 'r')
data = cust_profile.readlines()
cardNumber = input('Please enter your card Number:')
pin = input('Please enter your Pin Code:')
if cardNumber in data[0] and pin in data[1]:
    print('Login Successful')
    opt = int(input('Do you want to continue?\n Enter 0 to Display menu(Withdrawal, saving, current, other)\n 1 to Other Options(Pin Change, block card) \n 2 to Terminate: '))
    while True:
        if (opt == 0):
            print(
                'What would you like to do today? \n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Check Transaction History\n')
            opt = int(input('Enter your choice:'))
            if (opt == 1):
                depositcash()
                break
            elif (opt == 2):
                withdrawalcash()
                break
            elif (opt == 3):
                balance()
                break
            elif (opt == 4):
                transactionfilename = username + '_transactionhistory.txt'
                transactionfile = open(transactionfilename, 'a')
                with open(transactionfilename, 'r') as f:
                    f.seek(0)
                    if f.read(1):
                        print(f.read())
                        break
                    else:
                        print('There is no transaction history.')
                        break

                file.close()
            else:
                print('Wrong Option')
                opt = int(input('Do you want to continue? Select 0 to Continue, 1 to Terminate:'))
        elif (opt == 1):
            print('1. Pin Change \n 2 .Block card')
            opt = int(input('Enter your choice:'))
            if (opt == 1):
                pinChange()
            if(opt == 2):
                pass
            break
        elif (opt == 2):
            print('Goodbye')
            break
        else:
            print('Wrong option')
            opt = int(input('Do you want to continue? Select 0 to Continue, 1 to Terminate.'))
else:
    print('Incorrect Card Number or PinCode. Please try again later.')
