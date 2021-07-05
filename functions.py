import lists
import userlogin
from datetime import date
import os

account_list=lists.account_list  # list containg all account details
transaction_list=lists.transaction_list # list containing all transactions

# function call for clearing screen
def clear_screen():
    os.system('cls')

# function for cash withdrawal

def cash_withdraw(active_user,withdraw_amount):
    clear_screen()
    print("          Irish Bank")
    print("         ------------")
    for user in account_list:
        if user['Account_no']==active_user['Account_no']:
            active_balance=active_user['Account_balance']
            if (user['Account_balance']>=withdraw_amount):
                current_balance=user['Account_balance']
                current_balance=current_balance-withdraw_amount
                user['Account_balance']=current_balance
                count=len(transaction_list)
                id=count+1
                accno=user['Account_no']
                today_date=date.today()
                today_date=today_date.strftime("%x")
                type="Withdrawal"
                amount=withdraw_amount
                active_balance=active_balance-withdraw_amount
                transaction_list.append({"Transaction_id":str(id),"Account_no":str(accno),"Transaction_date":str(today_date),"Transaction_type":type,"Transaction_amount":amount,"Balance":active_balance})
                print("")
                print("Transaction completed")
                print("")
                print("please take your cash")
                print("")
                print("Thank you for choosing Irish Bank")
                print("")
                input("Return enter to continue...")
                clear_screen()
                userlogin.main_menu()
            else:
                #userlogin.clear_screen()
                print("")
                print("Insufficient Funds")
                print("")
                print("Transaction not completed")
                print("")
                input("Press enter to return to main menu.")
                clear_screen()
                userlogin.main_menu()

# function for cash lodging

def cash_deposit(active_user):
    clear_screen()
    print("          Irish Bank")
    print("         ------------")
    for user in account_list:
        if user['Account_no']==active_user['Account_no']:
            active_balance=active_user['Account_balance']
            deposit_amount=int(input("Enter the amount to be deposited :  "))
            current_balance=user['Account_balance']
            current_balance=current_balance+deposit_amount
            user['Account_balance']=current_balance
            count=len(transaction_list)
            id=count+1
            accno=user['Account_no']
            today_date=date.today()
            today_date=today_date.strftime("%x")
            type="Lodgement"
            amount=deposit_amount
            active_balance=active_balance+deposit_amount
            transaction_list.append({"Transaction_id":str(id),"Account_no":str(accno),"Transaction_date":str(today_date),"Transaction_type":type,"Transaction_amount":amount,"Balance":active_balance})
            print("")
            print("Transaction completed")
            print("")
            print("Thank you for choosing Irish Bank")
            print("")
            input("Press enter to return to main menu.")
            clear_screen()
            userlogin.main_menu()

#function for generating mini statement

def generate_report(active_user):
    print("Account Balance     :   ",active_user['Account_balance'])
    print("--------------------------------------------------------------------")
    print("Transaction Id      Date        Type     Amount      AccountBalance")
    print("---------------------------------------------------------------------")
    for user in transaction_list:
        if user['Account_no']==active_user['Account_no']:
             print(f"{user['Transaction_id'].ljust(17)} {user['Transaction_date'].ljust(12)} {user['Transaction_type'].ljust(10)} {user['Transaction_amount']}        {user['Balance']}") #display_users()
    print("-----------------------------------------------------------------------")
# function for changing pin

def change_pin(active_user):
    for user in account_list:
        if user['Account_no']==active_user['Account_no']:
            new_pin=input("Enter your new pin    : ")
            reentry=input("Confirm your new pin  : ")
            if(new_pin==reentry):
                user['Password']=new_pin
                clear_screen()
                print("Pin updated, Please Sign-in")
                print("")
                userlogin.user_login() 
            else:
                print("pin doesn't match")
                userlogin.main_menu()


       


   