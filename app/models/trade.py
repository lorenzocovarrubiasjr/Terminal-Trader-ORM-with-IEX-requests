import sqlite3
import os
from app.models.orm import ORM

class Trade(ORM):
    dbpath = os.path.join('data', 'trader.db')
    tablename = "trades"
    fields = ["stock_symbol", "account_pk", "type", "quantity", "created_at"]
    
    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.stock_symbol = kwargs.get("stock_symbol")
        self.account_pk = kwargs.get("account_pk")
        self.type = kwargs.get("type")
        self.type = kwargs.get("quantity")
        self.created_at = kwargs.get("created_at")