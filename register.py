from database import *
from customer import *
import random
from bank import *
from passwords import *
import customer

def signup():
    username=input("Please, enter the username: ")
    temp=query(f"select * from customers where username='{username}';")
    if temp:
        print("the username is already taken, please select another one")
        signup()
    else:
        print("username is free to use, please proceed")
        password=createPassword()
        print(password)
        name=input("enter the name:")
        age=int(input("enter the age:"))
        city=input("enter the city:")
        while True:
            account_number=random.randint(10000000,99999999)
            temp=query(f"select * from customers where account_number='{account_number}';")
            if temp:
                continue
            else:
                break
        status=input("enter the status:")
    cobj=Customer(username,password,name, age, city,account_number,status )
    cobj.createUser()
    bobj=Bank(username,account_number)
    bobj.create_transaction_table()
def signin():
    while True:
        username=input("Enter the username: ")
        temp=query(f"select * from customers where username='{username}';")
        if temp:
            while True:
                passw=input("Enter the password:")
                temp=query(f"select password from customers where username='{username}'")
                if passw==temp[0][0]:
                    print("login successful")
                    return username
                else:
                    print("password is incorrect, try again!")
            break
        else:
            print("Incorrect username, please enter a valid username")
            signin()

