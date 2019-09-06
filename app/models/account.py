import sqlite3
from app.models.orm import ORM
from app.models.position import Position
import app.models.util as util
from app.models.trade import Trade
import app.views as views
import random
import os
from time import strftime, localtime

class Account(ORM):
    #DIR = os.path.dirname("app") #__file__
    dbpath = os.path.join('data', 'trader.db')
    tablename = "accounts"
    fields = ["full_name", "pin", "balance", "account_number"]
    
    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.full_name = kwargs.get("full_name")
        self.pin = kwargs.get("pin")
        self.balance = kwargs.get("balance")
        self.account_number = kwargs.get("account_number", str(random.randint(0,10000000)))
        
    def deposit(self, amount):
        self.balance += amount
        views.display_balance(self.balance)
        self.save()
        return self.balance
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            views.display_balance(self.balance)
            self.save()
            return self.balance
    
    @classmethod
    def validate(cls, account_number, pin):
        if cls.one_from_where_clause("WHERE account_number = ? and pin = ?", [account_number, pin]):
            return True
        else:
            print("Sorry You are NOT a member. Join Now by Creating an Account for Free!")
            return None
    @classmethod    
    def load_account(cls, account_number, pin):
        loaded_account = Account.one_from_where_clause("WHERE account_number = ? and pin = ?", [account_number, pin])
        loaded_account.pk = loaded_account.pk
        loaded_account.full_name = loaded_account.full_name
        loaded_account.pin = loaded_account.pin
        loaded_account.balance = loaded_account.balance
        loaded_account.account_number = loaded_account.account_number
        return loaded_account
    
    def positions(self):
        positions = Position.all_from_where_clause("WHERE account_pk = ?", [self.pk])
        for stock in positions:
            print(stock.symbol, stock.amount)
        return positions

    def buy(self):
        stock_symbol = input("Which stock would you like to purchase?")
        stock_price = util.get_stock_current_price(stock_symbol)
        print("The stock price currently is: ",stock_price)
        quantity = float(input("How many shares would you like to purchase?"))
        cost = float(stock_price) * quantity
        if self.balance < cost:
            print("Sorry you do not have enough funds to complete this transaction.")
        else:
            self.balance -= cost
            position = Position.one_from_where_clause("WHERE account_pk = ? and symbol = ?", [self.pk, stock_symbol])
            if position != None:
                position.amount += quantity
                position.save()
            else:
                position_values = {"symbol": stock_symbol, "account_pk": self.pk, "amount" : quantity}
                position = Position(**position_values)
                position.save()
            time_of_trade = strftime("%b %d %Y %H:%M:%S", localtime())
            values = {"stock_symbol": stock_symbol, "account_pk": self.pk, "type": "BUY", "quantity": quantity, "created_at": time_of_trade}
            trade = Trade(**values)
            trade.save()
            self.save()
            
    def sell(self):
        stock_symbol = input("Which stock would you like to sell?")
        position = Position.one_from_where_clause("WHERE account_pk = ? and symbol = ?",[self.pk, stock_symbol])
        if position != None:
            stock_price = util.get_stock_current_price(stock_symbol)
            print("The stock price currently is: ",stock_price)
            quantity = float(input("How many shares would you like to sell?"))
            if quantity > position.amount:
                print("Sorry you do not own that many shares in this stock.")
            else:
                cost = float(stock_price) * quantity
                position.amount -= quantity
                position.save()
                self.balance += cost 
                self.save()
                time_of_trade = strftime("%b %d %Y %H:%M:%S", localtime())
                values = {"stock_symbol": stock_symbol, "account_pk": self.pk, "type": "SELL", "quantity": quantity, "created_at": time_of_trade}
                trade = Trade(**values)
                trade.save()
        else:
            print("Sorry, you do not have any shares in this stock.")
            
            