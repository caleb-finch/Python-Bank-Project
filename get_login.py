## Make a code that has a user login to their account and can do 5 functions. Deposit, Withdrawal, Balance Inquiry, Transfer Balance, Logout

#This is the get_login script. What this does is authenticate the user. The plan is to allow 3 fails before logging the user out and ending the program.




def get_login():
    wrong = 0
    authentication = 0
    
    while wrong < 3 and authentication == 0:
        username = str(input(f'Please enter your username: '))
        password = str(input(f'Please enter your password: '))
        
        if username == 'cfinch' and password == '12345': #this is the correct username and password
            authentication = 1
            savingsAmnt = 2000
            checkingsAmnt = 1000
            
        else:
            authentication = 0
            savingsAmnt = 0
            checkingsAmnt = 0
            username = 'error'
            wrong = 1 + wrong
            if wrong < 3:
                print(f'This is the incorrect username or password. You have {3 - wrong} chances left before logout!')
                
            else:
                print(f'You have entered the incorrect username or password too many times. Logging out!')

    return authentication, savingsAmnt, checkingsAmnt, username
        
        
get_login()



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