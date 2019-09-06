from app import views
from app.models import account, orm, position, trade, util
from app.models.account import Account
from app.models.position import Position
from app.models.trade import Trade
import app.models.util
import time

def login_loop():
    views.login_welcome()
    while True:
        views.display_login_menu()
        choice = views.get_login_choice()
        if int(choice) > 3:
            print("That is not an option!")
        #CREATE AN ACCOUNT																					
        elif int(choice) == 1:																										
            print("-----Create an Account-----")																								
            full_name = input("What is your full name?: ")	
            values = {"full_name":full_name, "pin": views.input_new_pin(), "balance": 0.00}		
            new_account = Account(**values)
            new_account.save()													
            print("Account Created! Your account number is:", new_account.account_number)													
            continue
        #LOGIN TO EXISTING ACCOUNT										
        elif int(choice) == 2:	
            account_num = views.get_login_num()
            pin = views.input_pin()
            if Account.validate(account_num, pin) == True: 
                loaded_account = Account.load_account(account_num, pin)
                print("This is your loaded account: ", loaded_account.account_number)
                return loaded_account
        #EXIT PROGRAM
        elif int(choice) == 3:													
            break															

def main_loop(account):																											
    views.space()																
    views.main_menu_welcome(account)										
    views.space()																
    while True:																	
        views.display_main_menu()												
        choice = views.get_login_choice()	
        try: 								
            if int(choice) > 5:
                print("That is not an option!")
                views.space()
        #DEPOSIT MONEY INTO ACCOUNT
            elif int(choice) == 1:
                account.deposit(float(input("How much would you like to deposit? ")))
        #WITHDRAW MONEY FROM ACCOUNT
            elif int(choice) == 2:
                account.withdraw(float(input("How much would you like to withdraw?")))
        #PURCHASE STOCK
            elif int(choice) == 3:
                account.buy()
                views.main_menu_welcome(account)
        #SELL STOCK
            elif int(choice) == 4:
                account.sell()
                views.main_menu_welcome(account)
            elif int(choice) == 5:
                break
        #LOG OUT
        except ValueError:
            print("Sorry, Not a Valid Choice!")
            pass

def run():
    while True:
        account = login_loop()
        if account is not None:
            main_loop(account)
            continue
        else:
            views.goodbye()
            break

if __name__ == '__main__':
    run()
