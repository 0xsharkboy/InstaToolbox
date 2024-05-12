from colorama import Fore
import os


ascii_art = """
 /$$$$$$                       /$$            /$$$$$$$$                  /$$ /$$                          
|_  $$_/                      | $$           |__  $$__/                 | $$| $$                          
  | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$  /$$$$$$   /$$$$$$ | $$| $$$$$$$   /$$$$$$  /$$   /$$
  | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$ /$$__  $$ /$$__  $$| $$| $$__  $$ /$$__  $$|  $$ /$$/
  | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$  \ $$| $$  \ $$| $$| $$  \ $$| $$  \ $$ \  $$$$/ 
  | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$  >$$  $$ 
 /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$|  $$$$$$/|  $$$$$$/| $$| $$$$$$$/|  $$$$$$/ /$$/\  $$
|______/|__/  |__/|_______/    \___/   \_______/|__/ \______/  \______/ |__/|_______/  \______/ |__/  \__/
                                                                                                          
***********************************************************************************************************"""

def banner(str):
  os.system('cls' if os.name == 'nt' else 'clear')
  print(Fore.RED + ascii_art)
  print(Fore.WHITE + str)