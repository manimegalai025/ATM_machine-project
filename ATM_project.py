from unittest import result
import random
import time
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    port="1124",
    user="root",
    password="mani",
    database="mmmatm_db"
    
)
mycursor=mydb.cursor()
def insert_data(User_pin,OTP,Balance,Withdraw_amount,Deposit_amount,current_balance):
    sql="insert into atm_machine(User_pin,OTP,Balance,Withdraw_amount,Deposit_amount,current_balance) values (%s,%s,%s,%s,%s,%s)"
    val=(User_pin,OTP,Balance,Withdraw_amount,Deposit_amount,current_balance)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data inserted successfully")
def view_data():
    mycursor.execute("select * from atm_machine")
    result=mycursor.fetchall()
    for i in result:
        print(i)
print("****************************************************************************")
print("* .-.-.-.-.-.-.-.-.                             -.-.-.-.-.-.-.-.-.-.-.-.-. *")
print("*  !!!                    WELCOME TO MMM ATM                            !!!*")
print("* ^_^_^_^_^_^_^_^_                              ^_^_^_^_^_^_^_^_^_^_^_^_   *")
print("****************************************************************************")

while True:
    break
print("               Please insert your ATM card...................!!            ")
time.sleep(3)
print("               Please wait while your card is being processed........")
time.sleep(5)
print("your ATM card inserted successfully")
print("*******         Do not remove the card till the transaction is completed           *******")
time.sleep(2)
print("&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&")
User_pin=int(input("Enter your ATM pin:"))
print("*&*&*&*&**&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&")
while User_pin < 1000 or User_pin > 9999:
    User_pin= int(input("\nInvalid pin.. Re-enter your pin[pin should be in 4 digits]: "))
    print("****************************************")
print("                wait for few mintues OTP will sentto your mobile no")
time.sleep(3)
print(random.randint(1000,9999))
print("$#$#$#$#$#$#$#$#$#$#$#$#$#$#$$#$#$##$#$#$$#")
OTP=int (input("please enter your otp:"))
print("your otp is valid")
while OTP < 1000 or OTP > 9999:
    OTP= int(input("\nInvalid otp.. Re-enter: "))
    print("..........................................")    

 
time.sleep(2)       


print("1. savings A/c     2. current A/c")
account_type=int(input("Enter your account type:"))
if account_type==1:
    print("your account type is savings")
    print("><><><><><><><><><><><><><><><><")
else:
    account_type==2
Balance=5000
current_balance=0

while True:
        print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
        try:
            option=int(input("please enter your choice:"))
        except:
            print("please enter valid  option")
        if option==1:
            print(f"your current balance is {Balance}")
            
        elif option==2:

            Withdraw_amount=int(input("please enter withdraw_amount:"))    
            Balance=Balance-Withdraw_amount
            print(f"{Withdraw_amount} is debited from your account")
            print("...........      Please take your cash     ........")
            time.sleep(3)
            print("your cash debited successfully........!!!")
            print(f"your current balance is {Balance}")

        elif option==3:

            Deposit_amount=int(input("please enter deposit_amount:"))    
            Balance=Balance+Deposit_amount
            print("............         please put your cash          .......")
            time.sleep(3)
            print("your cash credited successfully........!!!")
            print(f"{Deposit_amount} is credited to your account")
            print(f"your current balance is {Balance}")
            
        elif option==4:
            
            current_balance=int(input(f"your current_balance is:"))
            print(f"your current balance is {current_balance}")
            print("---------------------------------------------")
            print("exit")
            print("---------------------------------------------")
            print("please remove your ATM card")
            print("!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*")
            print("*                                           *")
            print("Thank you ...!!!  visit again......!!!!!")
            print("*                                      *")
            print(".............................................")
            break
        else:
            print("invalid option ")
        
insert_data(User_pin,OTP,Balance,Withdraw_amount,Deposit_amount,current_balance)
view_data()             


    

