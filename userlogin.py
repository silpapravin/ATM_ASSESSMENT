import os
import lists
import functions
from datetime import date, datetime

account_list=lists.account_list
fname=""
sname=""
type=""
balance=0
accno=0
withdraw_amount=0

# function to clear the screen
def clear_screen():
    os.system('cls')


# function for user login
def user_login():
    #clear_screen()
    print("         Welcome to Irish Bank")
    print("         ---------------------")
    user_name=input("Enter your username:     ")
    found=False
    for user in account_list:
        if (user['User_name']==user_name):
           pass_word=input("Enter your pincode :     ")
           if (user['Password']==pass_word):
              found=True
              global accno
              accno=user['Account_no']
              global fname
              fname=user['Account_fname']
              global sname
              sname=user['Account_sname']
              global overdraft
              overdraft=user['Overdraft_facility']
              global balance
              balance=user['Account_balance']
              global active_user
              active_user=user
              break
           else:
                found=False
                break;
    if found==True:
        clear_screen()
        print("Welcome",fname," ",sname)
        print("Login Successful")
        print("")
        #display_account()
        main_menu()
    else:
        answer=input("Login Unsuccessful...Do you want to try again [y/n] ")
        answer=answer.upper()
        if answer=="Y":
            clear_screen()
            user_login()
        else:
            clear_screen()
            print("Thankyou for using Irish bank")

# function to display user account details
def display_account():

    print("          Irish Bank")
    print("         ------------")
   
    print("Account Number      :   ",accno)
    print("First Name          :   ",fname)
    print("Second Name         :   ",sname)
    print("Overdraft Facility  :   ",overdraft)

# function to call  main menu to display services available
def main_menu():
    print("")
    print("          Irish Bank")
    print("         ------------")
    print("MENU OPTIONS")
    print("--------------")
    print(" 1 .   Check Balance ")
    print(" 2 .   Cash Withdrawal ")
    print(" 3 .   Cash Deposit ")
    print(" 4 .   Print Mini Statement ")
    print(" 5 .   Change Pin")
    print(" 6 .   Exit")
    choice=input("Please enter your choice [1/2/3/4/5/6]")
    if(choice=="1"):
        check_balance(active_user)
    elif (choice=="2"):
        global withdraw_amount
        withdraw_amount=cash_withdrawal_menu()            
        
    elif (choice=="3"):
        print("     CASH DEPOSIT")
        print("     ---------------")
        functions.cash_deposit(active_user)
    elif(choice=="4"):
        clear_screen()
       
        print("        Account Statement")
        print("        -----------------")
        print("Date :   ", date.today())
        print("")
        display_account()
        functions.generate_report(active_user)
        input("Press enter to return to main menu.")
        clear_screen()
        main_menu()
    elif(choice=="5"):
        clear_screen()
        print("    PIN CHANGE")
        print("    ----------")
        print("")
        choice=input("Do you want to change your pin [y/n]")
        choice=choice.upper()
        if (choice=="Y"):
           functions.change_pin(active_user)  
        else:
            print("Pin change canelled")
            input("Enter return to continue...")
            clear_screen()
            main_menu()
    elif(choice=="6"):
        exit()
    else:
        clear_screen()
        print("Invalid entry, Try again....")
        main_menu()
    
# function call to check account balance

def check_balance(active_user):
    clear_screen()
    display_account()
    print("Account Balance     :   ",active_user['Account_balance'])
    print("")
    input("press enter to return to main menu")
    clear_screen()
    main_menu()


################function for cash withdrawal menu###

def cash_withdrawal_menu():
        withdraw_choice=""
        withdraw_amount=0
        clear_screen()
        print("")
        print("     CASH WITHDRAWAL")
        print("     ---------------")
        print("  1.  20")
        print("  2.  40")
        print("  3.  60")
        print("  4.  80")
        print("  5.  100")
        print("  6.  Other amount")
        print("")
        withdraw_choice=input("Please enter your choice  :   ")
        if(withdraw_choice=="1"):
            withdraw_amount=20
            functions.cash_withdraw(active_user,withdraw_amount)
           
        
        elif(withdraw_choice=="2"):
            withdraw_amount=40
            functions.cash_withdraw(active_user,withdraw_amount)
        
        elif(withdraw_choice=="3"):
            withdraw_amount=60
            functions.cash_withdraw(active_user,withdraw_amount)
        
        elif(withdraw_choice=="4"):
            withdraw_amount=80
            functions.cash_withdraw(active_user,withdraw_amount)
        
        elif(withdraw_choice=="5"):
            withdraw_amount=100
            functions.cash_withdraw(active_user,withdraw_amount)
        
        elif(withdraw_choice=="6"):
            withdraw_amount=int(input("Enter the amount  :  "))
            if(withdraw_amount>500):
                print(" Maximum withdrawal in a transaction is 500..please try again")
                input("Please enter to return.....")
                cash_withdrawal_menu()
            else:
                functions.cash_withdraw(active_user,withdraw_amount)
        else:
            print("Invalid Entry..Please try again....")
            cash_withdrawal_menu()
        
        

