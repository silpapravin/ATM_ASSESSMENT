account_list=[]
transaction_list=[]

# list for account details
def create_accountlist():
    account_list.append({"Account_no": "1000", "Account_fname": "Fergus", "Account_sname": "Deffely", "Overdraft_facility": "YES", "Account_balance":6500.00, "User_name": "fergusdeffely", "Password":"1234"})
    account_list.append({"Account_no": "1001", "Account_fname": "John", "Account_sname": "Murphy", "Overdraft_facility": "YES", "Account_balance":4400.00, "User_name": "johnmurphy", "Password":"2020"})
    account_list.append({"Account_no": "1002", "Account_fname": "Aoife", "Account_sname": "Healy", "Overdraft_facility": "YES", "Account_balance":5000.00, "User_name": "aoifehealy", "Password":"1464"})
    account_list.append({"Account_no": "1003", "Account_fname": "Kevin", "Account_sname": "O'Brien","Overdraft_facility": "YES", "Account_balance":5000.00, "User_name": "kevinobrein", "Password":"5785"})
    account_list.append({"Account_no": "1004", "Account_fname": "Silpa", "Account_sname": "Pravin", "Overdraft_facility": "YES", "Account_balance":4900.00, "User_name": "silpapravin", "Password":"1980"})
    account_list.append({"Account_no": "1005", "Account_fname": "Fiona", "Account_sname": "Murphy", "Overdraft_facility": "YES", "Account_balance":4100.00, "User_name": "fionamurphy", "Password":"2020"})
    account_list.append({"Account_no": "1006", "Account_fname": "Marie", "Account_sname": "Lynch", "Overdraft_facility": "YES", "Account_balance":5120.00, "User_name": "marylynch", "Password":"1963"})
    account_list.append({"Account_no": "1007", "Account_fname": "Patrik", "Account_sname": "Brennan","Overdraft_facility": "YES", "Account_balance":900.00, "User_name": "patrikbrennan", "Password":"1111"})

# list for transaction details

def create_transactionlist():
    transaction_list.append({"Transaction_id":"1","Account_no":"1000","Transaction_date":"01/01/20","Transaction_type":"Lodgement","Transaction_amount":100,"Balance":5000.00})
    transaction_list.append({"Transaction_id":"1","Account_no":"1004","Transaction_date":"01/01/20","Transaction_type":"Lodgement","Transaction_amount":100,"Balance":5000.00})
    transaction_list.append({"Transaction_id":"2","Account_no":"1004","Transaction_date":"15/01/20","Transaction_type":"Withdrawal","Transaction_amount":1000,"Balance":4000.00})
    transaction_list.append({"Transaction_id":"3","Account_no":"1004","Transaction_date":"02/02/20","Transaction_type":"lodgement","Transaction_amount":500,"Balance":4500.00})
    transaction_list.append({"Transaction_id":"4","Account_no":"1005","Transaction_date":"01/03/21","Transaction_type":"Withdrawal","Transaction_amount":230,"Balance":5000.00})
    transaction_list.append({"Transaction_id":"5","Account_no":"1005","Transaction_date":"10/10/20","Transaction_type":"Lodgement","Transaction_amount":1500,"Balance":6500.00})
    transaction_list.append({"Transaction_id":"6","Account_no":"1001","Transaction_date":"07/03/21","Transaction_type":"Withdrwal","Transaction_amount":100,"Balance":5000.00})
    transaction_list.append({"Transaction_id":"7","Account_no":"1001","Transaction_date":"01/01/21","Transaction_type":"Withdrawal","Transaction_amount":600,"Balance":4400.00})
    transaction_list.append({"Transaction_id":"8","Account_no":"1002","Transaction_date":"15/05/21","Transaction_type":"Lodgement","Transaction_amount":100,"Balance":5000.00})
    transaction_list.append({"Transaction_id":"9","Account_no":"1003","Transaction_date":"28/04/21","Transaction_type":"Withdrawal","Transaction_amount":800,"Balance":5000.00})
    transaction_list.append({"Transaction_id":"10","Account_no":"1005","Transaction_date":"28/02/21","Transaction_type":"Withdrawal","Transaction_amount":4100,"Balance":2400.00})
    transaction_list.append({"Transaction_id":"11","Account_no":"1005","Transaction_date":"01/06/21","Transaction_type":"Lodgement","Transaction_amount":600,"Balance":3000.00})
    transaction_list.append({"Transaction_id":"12","Account_no":"1005","Transaction_date":"13/06/21","Transaction_type":"Lodgement","Transaction_amount":1100,"Balance":4100.00})
    transaction_list.append({"Transaction_id":"13","Account_no":"1006","Transaction_date":"28/05/21","Transaction_type":"Withdrawal","Transaction_amount":150,"Balance":5000.00})
    transaction_list.append({"Transaction_id":"14","Account_no":"1006","Transaction_date":"01/01/21","Transaction_type":"Lodgement","Transaction_amount":120,"Balance":5120.00})
    transaction_list.append({"Transaction_id":"15","Account_no":"1004","Transaction_date":"20/06/21","Transaction_type":"Lodgement","Transaction_amount":400,"Balance":4900.00})
    transaction_list.append({"Transaction_id":"16","Account_no":"1000","Transaction_date":"20/06/21","Transaction_type":"Lodgement","Transaction_amount":400,"Balance":5400.00})
    transaction_list.append({"Transaction_id":"17","Account_no":"1000","Transaction_date":"02/02/21","Transaction_type":"Lodgement","Transaction_amount":100,"Balance":5500.00})
    transaction_list.append({"Transaction_id":"18","Account_no":"1000","Transaction_date":"10/03/21","Transaction_type":"Lodgement","Transaction_amount":100,"Balance":5600.00})
    transaction_list.append({"Transaction_id":"19","Account_no":"1000","Transaction_date":"21/04/21","Transaction_type":"Lodgement","Transaction_amount":1000,"Balance":6600.00})
    transaction_list.append({"Transaction_id":"21","Account_no":"1000","Transaction_date":"01/01/21","Transaction_type":"Withdrawal","Transaction_amount":100,"Balance":6500.00})



