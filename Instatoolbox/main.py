from core.banner.banner import banner
from core.client.connect import connect

def main():
    banner("Welcome to InstaToolbox V1.0! \n")
    cl = connect()

if (__name__ == "__main__"):
    main()