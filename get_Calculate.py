## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout
##account = 1 is saving =2 is checking

##This is where we will calculate the accounts so we can get the updated amounts and can send this to output.

def get_Calculate(account_Info,  function_Input, savingsAmnt, checkingsAmnt, transaction):
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
            
    return checkingsAmnt, savingsAmnt