import os
from instagrapi import *
from colorama import Fore
import getpass
import tools

ascii_art = """
  /$$$$$$                       /$$            /$$$$$$$$                  /$$ /$$                          
 |_  $$_/                      | $$           |__  $$__/                 | $$| $$                          
   | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$  /$$$$$$   /$$$$$$ | $$| $$$$$$$   /$$$$$$  /$$   /$$
   | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$ /$$__  $$ /$$__  $$| $$| $$__  $$ /$$__  $$|  $$ /$$/
   | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$  \ $$| $$  \ $$| $$| $$  \ $$| $$  \ $$ \  $$$$/ 
   | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$  >$$  $$ 
  /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$|  $$$$$$/|  $$$$$$/| $$| $$$$$$$/|  $$$$$$/ /$$/\  $$
 |______/|__/  |__/|_______/    \___/   \_______/|__/ \______/  \______/ |__/|_______/  \______/ |__/  \__/
                                                                                                           
************************************************************************************************************"""
def banner(str):
  os.system('cls' if os.name == 'nt' else 'clear')
  print(Fore.RED + ascii_art)
  print(Fore.WHITE + str)
  
def menu():
  print("""Please select a tool :
  1. Get user info
  2. Get user followers
  3. Get user following
  4. Exit\n""")
  
def options(option, target):
    if option == '1':
        info(target)
    elif option == '2':
        followers(target)
    elif option == '3':
        following(target)
    elif option == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    else:
        print("Please select a valid option !")



cl = Client()

banner("Welcome to InstaToolbox V1.0! \n")
ACCOUNT_USERNAME = input("Enter your username/email : ")
ACCOUNT_PASSWORD = getpass.getpass("Enter your password (it won't be shown for security reasons) : ")

banner("Connecting...")
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

#getting user info
full_name = cl.account_info().dict()['full_name']
username = cl.account_info().dict()['username']
user_id = cl.account_info().dict()['pk']

banner("Succesfully connected !")

banner("Connected as " + full_name + " (" + username + ")" + " | " + user_id + "\n")

target = input("Enter the target username : ")

menu()
option = input("Enter your choice : ")
options(option)