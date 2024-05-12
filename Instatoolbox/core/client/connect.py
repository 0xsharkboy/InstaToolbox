from core.banner.banner import banner
from instagrapi import Client
import json

# Get account info
def account_info(cl):
    full_name = cl.account_info().dict()['full_name']
    username = cl.account_info().dict()['username']
    user_id = cl.account_info().dict()['pk']
    banner(f"Connected as {full_name} ({username}) | {user_id}")

# Load settings
def load_settings(cl, session_id, config, mode):

    # Check existing settings
    settings = False
    try:
        cl.load_settings('./settings.json')
        settings = True
    except:
        pass

    # Load settings
    if mode == "login":
        cl.login(config["username"], config["password"])
    else:
        cl.login_by_sessionid(str(session_id))

    # Save settings
    if (settings == False):
        cl.dump_settings('./settings.json')

# If two-factor authentification is enabled
def connect_by_sessionid(cl):
    print("Two-factor authentification is enabled on your account. Please use a session id to login.")
    session_id=input("Enter the session id : ")

    # Try to connect with session id
    try:
        load_settings(cl, session_id, "", "session")
        banner("Succesfully connected !")
        account_info(cl)
        return cl
    except:
        print("Error while connecting !")
        exit(1)

# Connect to Instagram
def connect():
    banner("Connecting...")

    # Create client
    cl = Client()

    # Load config
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Set proxy
    if (config["proxy"] != ""):
        cl.set_proxy(config["proxy"])

    # Try to connect with credentials
    try:
        load_settings(cl, "", config, "login")
        banner("Succesfully connected !")
        account_info(cl)
        return cl
    except Exception as e:
        if ("Two-factor authentication required" in str(e)):
            return connect_by_sessionid(cl)
        else:
            print("Error : " + str(e))
            exit(1)