#! /usr/bin/env python3

from app.models import account, orm, position, trade
from app.models.account import Account
from app.models.orm import ORM
from app.models.position import Position
from app.models.trade import Trade
from app import controller
import os 

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'trader.db')

controller.run()