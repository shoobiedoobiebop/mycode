#!/usr/bin/env python3
import robin_stocks.robinhood as r
from config import username, password

def login():
    r.login(username, password, expiresIn=86400, by_sms=True)

def logout():
    r.logout()

login()
logout()
#This serves as a proof of concept for logging in and out of robinhood.
