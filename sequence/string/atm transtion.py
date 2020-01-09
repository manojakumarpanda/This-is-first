#This program is for the atm transtion
def balanceinq(acno,uname,cur_balance,sav_balanc,branch,pin):
    balance=bal
    ac/no=int(input('Enter your account number for transtion:'))
    name=input('Enter your username for login to the account:')
    branc=input('Enter the branch name of the accout holder:')
    pin1=int(input('Enter your login pin:'))
    if branc == branch:                      #this will verify the branch name 
        if ac/no ==acno or name == uname: # this will verify the uname 
            if pin1== pin: #this will veerify the pin of the account holder
                print('Enter the type of the account you have')
                curr=input('Enter the current if you have current bank account')
                if curr ==  #this will veerify the type of the account 
                print('Your acount number is :{:d}with name {1} having balance is :{:10.2f} and name of the branch is:'.format(ac/no,name,balance),branch,sep=' ')
                return
            else:
                print('you have entered a wrong pin please verify it and retry again:')
        else:
            print('you have entered a wrong user name or acount number please verify it and retry again:')
    else:
        print('you have entered a wrong pin please verify it and retry again:')
    return
def diposite (acno,uname,cur_balance,sav_balance,branch,pin):
    accno=int(input('Enter your account number for transction:'))
    user=input('Enter your user name for the transction:')
    branc=input("Enter the branch name for the transtion:")
    pin1=int(input('Enter pin for the transction:'))
    if branc == branch:             #this will verify the branch name 
        if user == uname or accno == acno:# this will verify the uname
            if pin1== pin:    #this will veerify the pin of the account holder
                print('Enter the type of the account you have')
                curr=input('Enter the current if you have current bank account')
                if curr ==    #this will veerify the type of the account
                bal=float(input('Enter the amount you want to diposite:'))
                balance+=bal
            else:
                print('Your pin is invalid please check it')
                break
        else:
            print('You have entered a wrong username or account number please check:')
            break
    else:
        print('you heve visited to wrong bank :')
return balance
def withdraw(acno,uname,balance,branch,pin):
    accno=int(input('Enter the account number for the transction:'))
    user=input('Enter the username for the transction:')
    branc=input('Enter the branch name for the transction:')
    pin1=int(input('Enter the pin number for the transction:'))
    if branc == branch:    #this will verify the branch name 
        if user == uname or accno== acno:   # this will verify the uname
            if pin1 == pin:    #this will veerify the pin of the account holder
                print('Enter the type of the account you have')
                curr=input('Enter the current if you have current bank account')
                if curr ==     #this will veerify the type of the account
                bal=float(input('Enter the amount you want to withdraw from account:'))
                if bal >= balance:
                    print('You have a insufficent balance please visited nearest bank or check youer available balance:')
                else:
                    balance=balance-bal
                    repeat=input('if you want to check the available balance please enter yes or else no')
                    if repeat == 'yes' or 'YES':
                        print('You have a balance remaining in your account:',balance)
                    else:
                        print('Thanks for visiting visit again Thank You')
            else:
                print('Invalid credentionla Please verify the pin:')
        else:
            print('Invalid username or account number please verify the username and try again:')
    else:
        print('you have visited to a wrong bank atm please go and verify the bank or branch :')
    return
def change_pin(pin):
    temp=input('Do you want to change your password')
    if temp == 'yes' or 'YES':
        pin1=int(input('Enter the older password you have before:'))
        if pin1 == pin :    #this will veerify the pin of the account holder
            print('Enter the type of the account you have')
                curr=input('Enter the current if you have current bank account')
                if curr ==     #this will veerify the type of the account
            newpin=int(input('Enter the new passowrd you want to replace with :'))
            pin=newpin
        else:
            print('you have entered a wrong older pin please retry:')
            forget=input('for forget password input here yes:')
            if forget == 'yes'or'YES':
                pass #for now a time i wnat to pass this after have knowledge of random module i will go  to this
            elif forget == 'no' or 'NO' or 'No' or 'nO':
                pass #for now a time i wnat to pass this after have knowledge of random module i will go  to this
    print('Thank you for visiting our atm ')#for now a time i wnat to pass this after have knowledge of random module i will go  to this
    return
def change_uname(uname,acno):
    temp=input('Do you want to change your username ')
    if temp == 'yes' or 'YES':
        print('Enter the type of the account you have')
                curr=input('Enter the current if you have current bank account')
                if curr ==   #this will veerify the type of the account
        un=input('Enter the older username you have before:')
        if uname == un or accno== acno :# this will verify the uname
            newun=input('Enter the new username you want to replace with :')
            uname=newun
            newaccno=int(input('Enter the new account number you want to replace with:'))
        else:
            print('you have entered a wrong older pin please retry:')
            forget=input('for forget password input here yes:')
            if forget == 'yes'or'YES':
                pass #for now a time i wnat to pass this after have knowledge of random module i will go  to this
            elif forget == 'no' or 'NO' or 'No' or 'nO':
                pass #for now a time i wnat to pass this after have knowledge of random module i will go  to this
    print('Thank you for visiting our atm ')#for now a time i wnat to pass this after have knowledge of random module i will go  to this
    return
def forget_user_pin():
    pass
def ministatenet():
    pass
balanceinq()
diposite()
withdraw()
change_pin()
change_uname()
#forget_user_pin()
#ministatenet()










    
                
        

             
    
        
