import sqlite3
from app.models.orm import ORM
import os

class Position(ORM):
    dbpath = os.path.join('data', 'trader.db')
    tablename = "positions"
    fields = ["stock_symbol", "account_pk", "amount"]
    
    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.account_id = kwargs.get("account_pk")
        self.amount = kwargs.get("amount")
        self.stock_symbol = kwargs.get("symbol")
    
    
        
