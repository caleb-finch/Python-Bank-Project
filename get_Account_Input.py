## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout

## The user wants to do 1 of 5 functions for their savings or checkings account.

##account = 1 is saving =2 is checking


def get_Account_Input(account_Info, savingsAmnt, checkingsAmnt):
    function_Input = 0
    
    while function_Input > 5 or function_Input < 1:
        try:
            function_Input = int(input(f'1 = Deposit \n2 = Withdrawal\n3 = Balance Inquiry \n4 = Transfer Balance \n5 = Log Out\nWhat would you like to do? '))
            
            if function_Input == 1:
                print(f'Deposit option has been chosen')
                transaction = int(input(f'How much do you want to deposit? (Cannot exceed $500):'))
                
            if function_Input == 2:
                print(f'Withdraw option has been chosen')
                if account_Info == 1:
                    transaction = int(input(f'How much do you want to withdraw? (Cannot exceed $500):'))
                    print(f'savings amount = {savingsAmnt}\ntransaction amount = {transaction}')
                    while (savingsAmnt <= transaction) or (0 > transaction) or (transaction > 500):
                        print(f'ERROR! Withdraw amount exceeds accepted amount or is less than 0.')
                        print(f'savings amount = {savingsAmnt}\ntransaction amount = {transaction}')
                        transaction = int(input(f'How much do you want to withdraw? (Cannot exceed $500):'))
                else:
                    transaction = int(input(f'How much do you want to withdraw? (Cannot exceed $500):'))
                    while (checkingsAmnt <= transaction) or (0 > transaction) or (transaction > 500):
                        print(f'ERROR! Withdraw amount exceeds accepted amount or is less than 0.')
                        transaction = int(input(f'How much do you want to withdraw? (Cannot exceed $500):'))
                        
            if function_Input == 3:
                transaction = 0
                print(f'Balance Inquiry option has been chosen')
                
            if function_Input == 4:
                print(f'Transfer option has been chosen')
                if account_Info == 1:
                    transaction = int(input(f'How much do you want to transfer? (Cannot exceed $500):'))
                    while (checkingsAmnt <= transaction) or (0 > transaction) or (transaction > 500):
                        print(f'ERROR! Withdraw amount exceeds accepted amount or is less than 0.')
                        transaction = int(input(f'How much do you want to withdraw? (Cannot exceed $500):'))
                else:
                    transaction = int(input(f'How much do you want to transfer? (Cannot exceed $500):'))
                    while (savingsAmnt <= transaction) or (0 > transaction) or (transaction > 500):
                        print(f'ERROR! Withdraw amount exceeds accepted amount or is less than 0.')
                        transaction = int(input(f'How much do you want to withdraw? (Cannot exceed $500):'))
                        
            if function_Input == 5:
                transaction = 0
                print(f'Logout option has been chosen')
            
            else:
                print(f'Error! You have not typed a number from 1 - 5. Please try again.')
                
        except ValueError:
            print(f'Error! You have not typed a number from 1 - 5. Please try again.')
            
    return transaction, function_Input
        

#get_Account_Input(1, 2000, 1000)