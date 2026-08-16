## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout

#This is the get_login script. What this does is authenticate the user. The plan is to allow 3 fails before logging the user out and ending the program.

import csv
from pathlib import Path

def get_login():
    wrong = 0
    authentication = 0
    savingsAmnt = 0
    checkingsAmnt = 0
    
    base_dir = Path(__file__).resolve().parent
    db_candidates = [
        base_dir / 'bank_database.csv',
    ]

    # Read CSV file ONCE before asking for credentials
    csv_path = next((path for path in db_candidates if path.exists()), None)
    if csv_path is None:
        print(f'Error: bank database file not found!')
        return authentication, savingsAmnt, checkingsAmnt, 'error'

    try:
        users = {}
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users[row['username']] = row
                
    except FileNotFoundError:
        print(f'Error: bank database file not found!')
        return authentication, savingsAmnt, checkingsAmnt, 'error'

    # Now ask for credentials
    while wrong < 3 and authentication != 1:
        username = str(input(f'Please enter your username: '))
        password = str(input(f'Please enter your password: '))
        
        if username in users and password == '12345':
            authentication = 1
            savingsAmnt = int(users[username]['savingsAmnt'])
            checkingsAmnt = int(users[username]['checkingsAmnt'])
            
        if authentication == 0:
            savingsAmnt = 0
            checkingsAmnt = 0
            username = 'error'
            wrong = 1 + wrong
            if wrong < 3:
                print(f'This is the incorrect username or password. You have {3 - wrong} chances left before logout!')
                
            else:
                print(f'You have entered the incorrect username or password too many times. Logging out!')

    return authentication, savingsAmnt, checkingsAmnt, username
        
        
if __name__ == '__main__':
    result = get_login()
    print(result)



#def test2():
#    return 'abc', 100, [0, 1, 2]
#
#a, b, c = test2()
#
#print(a)
## abc
#
#print(b)
## 100
#
#print(c)
## [0, 1, 2]