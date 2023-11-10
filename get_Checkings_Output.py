## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout

#This is to output if the user chose to make changes to their savings account.

def get_Checkings_Output(account_Info, username, function_Input, savingsAmnt, checkingsAmnt, transaction):
	
    if function_Input == 1:
        print(f'{username} deposited ${transaction} to their checking account. Their new balance:\nSavings Account: ${savingsAmnt}\nChecking Account: ${checkingsAmnt}')
    if function_Input == 2:
        print(f'{username} withdrew ${transaction} from their checking account. Their new balance:\nSavings Account: ${savingsAmnt}\nChecking Account: ${checkingsAmnt}')
    if function_Input == 3:
        print(f'{username} balance:\nSavings Account: ${savingsAmnt}\nChecking Account: ${checkingsAmnt}')
    if function_Input == 4:
        print(f'{username} transferred ${transaction} from their savings account to their checking account. Their new balance:\nSavings Account: ${savingsAmnt}\nChecking Account: ${checkingsAmnt}')
        
#get_Checkings_Output('c', 'username', 2, 2000, 1000, 0)