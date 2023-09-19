import os
from instagrapi import *
from colorama import Fore
from art import *
import getpass

os.system('cls' if os.name == 'nt' else 'clear')

ascii_art = """
  /$$$$$$                                   /$$                      /$$$$$$
 /$$__  $$                                 | $$                     /$$__  $$
| $$  \__/  /$$$$$$  /$$$$$$  /$$  /$$  /$$| $$  /$$$$$$   /$$$$$$ | $$  \__/  /$$$$$$  /$$$$$$  /$$$$$$/$$$$
| $$       /$$__  $$|____  $$| $$ | $$ | $$| $$ /$$__  $$ /$$__  $$| $$ /$$$$ /$$__  $$|____  $$| $$_  $$_  $$
| $$      | $$  \__/ /$$$$$$$| $$ | $$ | $$| $$| $$$$$$$$| $$  \__/| $$|_  $$| $$  \__/ /$$$$$$$| $$ \ $$ \ $$
| $$    $$| $$      /$$__  $$| $$ | $$ | $$| $$| $$_____/| $$      | $$  \ $$| $$      /$$__  $$| $$ | $$ | $$ 
|  $$$$$$/| $$     |  $$$$$$$|  $$$$$/$$$$/| $$|  $$$$$$$| $$      |  $$$$$$/| $$     |  $$$$$$$| $$ | $$ | $$
 \______/ |__/      \_______/ \_____/\___/ |__/ \_______/|__/       \______/ |__/      \_______/|__/ |__/ |__/
 
"""
print(Fore.RED + ascii_art)
print(Fore.WHITE)

cl = Client()

ACCOUNT_USERNAME = input("Enter your username/email : ")
ACCOUNT_PASSWORD = getpass.getpass("Enter your password (it won't be shown for security reasons) : ")

print("Connecting...")
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.RED + ascii_art)
print(Fore.WHITE)

print("Succesfully connected !")
