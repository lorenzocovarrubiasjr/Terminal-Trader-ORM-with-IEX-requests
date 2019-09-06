import getpass
import time
import hashlib 

def login_welcome():
    # display your welcome message here
    print("""88888b.d88b.  .d88b. 88888b.  .d88b. 888  888 
888 "888 "88bd88""88b888 "88bd8P  Y8b888  888 
888  888  888888  888888  88888888888888  888 
888  888  888Y88..88P888  888Y8b.  ..Y88b 888 
888  888  888 "Y88P" 888  888 "Y8888" "Y88888 
                                          888 
                                     Y8b d88P 
                                       Y88P  """)
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
    encoded_pin = pin_num.encode("utf-8")
    secure_pin = hashlib.sha256(encoded_pin).hexdigest()
    return secure_pin

def input_pin():
    # check it out, emojis and hidden password entry
    pin_num = getpass.getpass(prompt="\U0001F512 Enter Your PIN#: ")
    encoded_pin = pin_num.encode("utf-8")
    secure_pin = hashlib.sha256(encoded_pin).hexdigest()
    return secure_pin

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
