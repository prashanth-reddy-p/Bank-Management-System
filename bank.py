from asyncio import current_task

from Demos.win32ts_logoff_disconnected import username
import datetime

from database import query


class Bank:
    def __init__(self, username, account_number):
        self.__username=username
        self.__account_number=account_number
    def create_transaction_table(self):
        query(f"create table if not exists {self.__username}_transactions (timedate DATETIME,account_number integer,remarks varchar(30), amount integer);")
    def balanceEnquiry(self):
        b=query(f"select balance from customers where username='{self.__username}';")
        return b[0][0]
    def cashDeposit(self, deposit_amount):
        current_balance=self.balanceEnquiry()
        deposit=deposit_amount+current_balance
        query(f"update customers set balance='{deposit}' where username='{self.__username}';")
        query(f"insert into {self.__username}_transactions values('{datetime.datetime.now()}','{self.__account_number}','amount deposit','{deposit_amount}')")
        print(f"amount deposited to your account:{deposit_amount}")
        print(f"your current balance is {self.balanceEnquiry()}")
    def cashWithdraw(self, withdraw_amount):
        current_balance = self.balanceEnquiry()
        if current_balance > withdraw_amount > 0:
            withdraw = current_balance-withdraw_amount
            query(f"update customers set balance='{withdraw}' where username='{self.__username}';")
            query(
                f"insert into {self.__username}_transactions values('{datetime.datetime.now()}','{self.__account_number}','amount withdrawn','{withdraw_amount}')")
            print(f"amount withdrawn from your account:{withdraw_amount}")
            print(f"your final balance is {self.balanceEnquiry()}")
        else:
            print("Insufficient balance, please try again with lesser amount")
    def fundTransfer(self, account_number, transfer_amount):
        while True:
            temp=query(f"select account_number from customers where account_number='{account_number}'")
            if temp:
                break
        current_balance=self.balanceEnquiry()
        receiver_name=query(f"select username from customers where account_number='{account_number}';")[0][0]
        if transfer_amount > current_balance:
            print("Insufficient funds to transfer")
        else:
            withdraw = current_balance - transfer_amount
            query(f"update customers set balance='{withdraw}' where username='{self.__username}';")
            query(
                f"insert into {self.__username}_transactions values('{datetime.datetime.now()}','{self.__account_number}','fund transfer to {account_number}','{transfer_amount}')")
            b = query(f"select balance from customers where account_number='{account_number}';")[0][0]
            updated_balance=b+transfer_amount

            query(f"update customers set balance='{updated_balance}' where account_number='{account_number}'")
            print("transaction successful")
            query(
                f"insert into {receiver_name}_transactions values('{datetime.datetime.now()}','{account_number}','fund transfer from {self.__account_number}','{transfer_amount}')")





