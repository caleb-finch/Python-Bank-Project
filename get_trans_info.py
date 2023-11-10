## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout

## This is the get_trans_info script where the code extracts asks the user how many transactions they want to make (max of 3 transcactions)

def get_trans_info():
    numTrans = 0
    while numTrans < 1 or numTrans > 3:
        try:
            numTrans = int(input(f'How many transactions would you like to do today? (Max of 3): '))
            if numTrans < 1 or numTrans > 3:
                print(f'Please type a number between 1 and 3.')
            else:
                print(f'{numTrans} transactions have been chosen.')
                
        except ValueError:
            print(f'Please type a number between 1 and 3.')
                
        
    return numTrans
    
#get_trans_info()

            