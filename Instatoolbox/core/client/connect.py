from core.banner.banner import banner
from instagrapi import Client
import json

def account_info(cl):
    full_name = cl.account_info().dict()['full_name']
    username = cl.account_info().dict()['username']
    user_id = cl.account_info().dict()['pk']
    banner(f"Connected as {full_name} ({username}) | {user_id}")

def connect_by_sessionid(cl):
    print("Two-factor authentification is enabled on your account. Please use a session id to login.")
    session_id=input("Enter the session id : ")
    try:
        cl.login_by_sessionid(str(session_id))
        banner("Succesfully connected !")
        account_info(cl)
        return cl
    except:
        print("Error while connecting !")
        exit(1)

def connect():
    banner("Connecting...")
    cl = Client()
    with open('config.json', 'r') as f:
        config = json.load(f)
    if (config["proxy"] != ""):
        cl.set_proxy(config["proxy"])
    try:
        cl.login(config["username"], config["password"])
        banner("Succesfully connected !")
        account_info(cl)
        return cl
    except Exception as e:
        if ("Two-factor authentication required" in str(e)):
            return connect_by_sessionid(cl)
        else:
            print("Error : " + str(e))
            exit(1)