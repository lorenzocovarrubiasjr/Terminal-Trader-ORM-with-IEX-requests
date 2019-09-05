import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'trader.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        
        SQL = "DROP TABLE IF EXISTS accounts;"
        cur.execute(SQL)
        
        SQL = """CREATE TABLE accounts (
            pk INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            full_name VARCHAR(128) NOT NULL,
            account_number VARCHAR(16) UNIQUE NOT NULL,
            pin VARCHAR(4) NOT NULL,
            balance FLOAT
        ); """
        cur.execute(SQL)
        
        SQL = "DROP TABLE IF EXISTS positions;"
        cur.execute(SQL)
        
        SQL = """CREATE TABLE positions (
            pk INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            symbol VARCHAR(128) NOT NULL,
            account_pk INTEGER NOT NULL,    
            amount FLOAT NOT NULL
        );"""
        cur.execute(SQL)
        
        SQL = "DROP TABLE IF EXISTS trades;"
        cur.execute(SQL)
    
        SQL = """ CREATE TABLE trades (
            pk INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            stock_symbol VARCHAR(128) NOT NULL,
            quantity FLOAT NOT NULL,
            account_pk INTEGER NOT NULL,
            type VARCHAR(128) NOT NULL,
            created_at VARCHAR(128)
        );"""
        cur.execute(SQL)