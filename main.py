
from register import *
from bank import *
print("                Hello, welcome to python bank")
status=False

while True:
    try:
        register=int(input("""
Please select the option:
1.signin
2.signup
3.quit
enter: """))
        if register==3:
            exit()
        elif register==1:
            user=signin()
            status=True
            break
        elif register==2:
            signup()
    except ValueError:
        print("please choose from the above option")

account_number=query(f"select account_number from customers where username='{user}'; ")[0][0]
while status:
    try:
        facility=int(input("""
Please select the option:
1.Balance Enquiry
2.Cash Deposit
3.Cash Withdraw
4.Fund Transfer
enter: """))
        if facility in range(1,6):
            bobj = Bank(user, account_number)
            if facility==1:
                print(f" Your current balance is {bobj.balanceEnquiry()}")
            elif facility==2:
                try:
                    deposit_amount = int(input("please enter the amount to deposit"))
                    if deposit_amount<0:
                        raise ValueError("Deposit amount cannot be negative.")
                    bobj.cashDeposit(deposit_amount)
                except ValueError as e:
                    print(e)


            elif facility==3:
                withdraw_amount = int(input("please enter the amount to withdraw"))
                bobj.cashWithdraw(withdraw_amount)

            elif facility==4:
                account_number=int(input("please enter the account number:"))
                amount=int(input("Enter the amount to transfer:"))
                bobj.fundTransfer(account_number,amount)
            elif facility==5:
                exit()

    except ValueError:
        print("please choose from the above option:")