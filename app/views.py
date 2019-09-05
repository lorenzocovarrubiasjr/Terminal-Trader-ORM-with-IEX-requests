import getpass
import time

def login_welcome():
    # display your welcome message here
    print("'''''''''''''WELCOME'''''''''''''''''")
    time.sleep(0.1)
    print("'''''''''''''''''''''''''''''''''''''")
    time.sleep(0.1)
    print("'''''Lorenzo's Terminal Trader'''''''")
    time.sleep(0.1)
    print("'''''''''''''''''''''''''''''''''''''")
    time.sleep(0.1)

def space():
    print("- = - = - = - = - = - = - = - = - = -")
    time.sleep(0.1)

def input_new_pin():
    # check it out, emojis and hidden password entry
    pin_num = getpass.getpass(prompt="\U0001F512 Choose a PIN#: ")
    return pin_num

def input_pin():
    # check it out, emojis and hidden password entry
    pin_num = getpass.getpass(prompt="\U0001F512 Enter Your PIN#: ")
    return pin_num

def display_login_menu():
    # display a menu with create account, login, and quit options
    print("1) Create Account")
    print("2) Login")
    print("3) Exit")
    print("")

def get_login_choice():
    choice = None
    choice = input("Please make a selection from the menu: ")
    return choice

def display_main_menu():
    # display a menu with check balance, deposit, withdraw, and exit options
    print("What would you like to do today?")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Purchase Stock") 
    print("4) Sell Stock")
    print("5) Log Out")

def main_menu_welcome(account):
    # some view functions will need arguments
    print("Welcome, {}".format(account.full_name))
    display_balance(account.balance)
    print("Your current positions are:")
    account.positions()
    print()

def display_balance(balance):
    # the controller should get specific data from the model, view functions
    # should only take simple values as their arguments and should not need
    # to call the model
    space()
    print("Your balance is ${:.2f}".format(balance))
    print()

def goodbye():
    print("Thank Your for visiting! Come back soon.")

def logout_message():
    space()
    space()
    print("Thank You for Your Business, Until next time!")
    space()
    space()

def get_login_num():
    attempted_login_num = input("What is your account number?:")
    return attempted_login_num
