import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "trader.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def seed(dbpath=DBPATH):
    accounts = [
        ("Lorenzo Covarrubias Jr.", "00000001", "1234", "1000.00")
        ]
    
    positions = [
        ("WMT",1,1.0),
        ("BYND",1,0.45),
        ("TSLA",1,10.0)
        ]
    trades = [
        ("TSLA",5.0, 1,"SELL",  "September 29 2018 15:55:67"),
        ("WMT", 1.0, 1, "BUY", "March 13, 2018 01:33:55"),
        ("BYND",0.45, 1,"BUY",  "January 31, 2018 11:45:46")
    ]
    
    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor()
        SQL = """INSERT INTO accounts(full_name,account_number,pin, balance) VALUES (?,?,?,?)"""
        for account in accounts:
            curs.execute(SQL, account)
            
        SQL = """INSERT INTO positions(symbol, account_pk, amount) VALUES (?,?,?)"""
        for position in positions:
            curs.execute(SQL, position)
            
        SQL = """INSERT INTO trades(stock_symbol,quantity, account_pk, type, created_at) VALUES (?,?,?,?,?)"""
        for trade in trades:
            curs.execute(SQL, trade)
            
