import os
import lists
import userlogin

account_list=lists.create_accountlist() 
transaction_list=lists.create_transactionlist()

def clear_screen():
    os.system('cls')

clear_screen()
userlogin.user_login()
