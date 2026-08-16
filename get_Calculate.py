## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout
##account = 1 is saving =2 is checking

##This is where we will calculate the accounts so we can get the updated amounts and can send this to output.
import csv

def save_account_balances(username, savingsAmnt, checkingsAmnt):
    with open('bank_database.csv', 'r', newline='') as csvfile:
        rows = list(csv.DictReader(csvfile))

    for row in rows:
        if row['username'] == username:
            row['savingsAmnt'] = str(savingsAmnt)
            row['checkingsAmnt'] = str(checkingsAmnt)

    with open('bank_database.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['username', 'savingsAmnt', 'checkingsAmnt'])
        writer.writeheader()
        writer.writerows(rows)

def get_Calculate(account_Info, function_Input, savingsAmnt, checkingsAmnt, transaction, username):
    if account_Info == 1:
        if  function_Input == 1:        #deposit
            savingsAmnt = savingsAmnt + transaction
        if function_Input == 2:         #withdraw
            savingsAmnt = savingsAmnt - transaction
        if function_Input == 4:         #transfer
            checkingsAmnt = checkingsAmnt - transaction
            savingsAmnt = savingsAmnt + transaction
            
    if account_Info == 2:
        if  function_Input == 1:        #deposit
            checkingsAmnt = checkingsAmnt + transaction
        if function_Input == 2:         #withdraw
            checkingsAmnt = checkingsAmnt - transaction
        if function_Input == 4:         #transfer
            savingsAmnt = savingsAmnt - transaction
            checkingsAmnt = checkingsAmnt + transaction


    save_account_balances(username, savingsAmnt, checkingsAmnt)

    return checkingsAmnt, savingsAmnt

if __name__ == '__main__':
    result = get_Calculate(1, 1, 1000, 500, 300, 'cfinch') #change to what you want to test
    print(result)