## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout

#This is the main script that calls to other scripts Here is the flow for the script
#Call to login_script --- Check if the login script authenticated the user, if it did then run get_transaction_info script --- run get_account_info script --- run function_input script --- run the calculate script --- run the output script .end

##Getting variables from modules
from get_login import get_login
from get_trans_info import get_trans_info
from get_Account_Info import get_Account_Info
from get_Account_Input import get_Account_Input
from get_Calculate import get_Calculate
from get_Savings_Output import get_Savings_Output
from get_Checkings_Output import get_Checkings_Output

##Main function
def main():
    print(f'Welcome to KMoney Bank!')
    #call the get_login script
    authentication, savingsAmnt, checkingsAmnt, username = get_login()
    
    if authentication == 0:
        print(f'You have entered the wrong username and/or password too many times!')
        
        
    if authentication == 1:
        print(f'AUTHENTICATED')
        numTrans = get_trans_info()
        #print(f'we are back in main. {numTrans}')
        transCounter = 0
        function_Input = 0
        while (transCounter != numTrans) and (function_Input != 5):
        
            ##Call script to get checking or saving account
            account_Info = get_Account_Info()
            
            ##Call script to find if deposit, withdraw, etc
            transaction, function_Input = get_Account_Input(account_Info, savingsAmnt, checkingsAmnt)
            
            ##Call script that manipulates checking/saving account with transaction variable
            checkingsAmnt, savingsAmnt = get_Calculate(account_Info, function_Input, savingsAmnt, checkingsAmnt, transaction)
            
            ##OUTPUT.
            #This is for savings account
            if account_Info == 1:
                get_Savings_Output(account_Info, username, function_Input, savingsAmnt, checkingsAmnt, transaction)
                
            #This is for checking account
            if account_Info == 2:
                get_Checkings_Output(account_Info, username, function_Input, savingsAmnt, checkingsAmnt, transaction)
                
            ##Keep track of how many transactions have been done
            transCounter = transCounter + 1
            
        print(f'{username} has been logged out!')
        
    
main()
