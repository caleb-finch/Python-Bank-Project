## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout

##Find out if the user wants to manipulate the savings or checkings account

def get_Account_Info():
    Account_info_string = 'account'
    while Account_info_string != 's' or  Account_info_string != 'c':

        Account_info_string = input(f'Do you want to be in Savings or Checkings acccount? For Transfer enter the account you want the money to go into. (Enter s or c)  ')
        if Account_info_string == 's':
            Account_Info = 1
            print(f'Savings Account has been chosen')
        if Account_info_string == 'c':
            Account_Info = 2
            print(F'Checking Account has been chosen')
            
        else:
            print(f"Error! You have not typed 's' or 'c'! Please try again.")
    return Account_Info
    
#get_Account_Info()