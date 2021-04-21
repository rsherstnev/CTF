#!/usr/bin/env python3 

import sys
from telebot import TeleBot

if len(sys.argv) == 2:
    TOKEN = 'ENTER HERE YOUR BOT TOKEN'
    ID = ENTER_HERE_YOUR_USER_ID
    TeleBot(TOKEN).send_message(ID, sys.argv[1])
else:
    print('Usage: botsend.py <message>')
