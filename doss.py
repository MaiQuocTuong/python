import random
import threading
import socket
import os
import time 
from termcolor import colored

os.system('cls')
print(colored(r"""
DDDDDDDDDDD               OOOOOOOOO           SSSSSSSSSSSS
D::::::::::DDD          OO:::::::::OO       SS::::::::::::S
D:::::::::::::DD      OO:::::::::::::OO    S:::::::::::::::S
DDD:::DDDDD:::::D    O:::::::OOO:::::::O  S::::::SSSSS:::::S
  D:::D    D:::::D  O:::::::O   O:::::::O S::::::S    SSSSSS
  D:::D     D:::::DO:::::::O     O:::::::OS::::::S
  D:::D     D:::::DO:::::::O     O:::::::OS::::::S
  D:::D     D:::::DO:::::::O     O:::::::O S::::::SSS
  D:::D     D:::::DO:::::::O     O:::::::O  SS::::::SSSS
  D:::D     D:::::DO:::::::O     O:::::::O    SSSSS:::::SS
  D:::D     D:::::DO:::::::O     O:::::::O         S::::::S
  D:::D    D:::::D  O:::::::O   O:::::::O          S::::::S
DDD:::DDDDD:::::D    O:::::::OOO:::::::O           S::::::S
D:::::::::::::DD      OO:::::::::::::OO    SSSS    S::::::S
D:::::::::::DDD         OO:::::::::OO      S:::SSSS::::::S
DDDDDDDDDDDD              OOOOOOOOO         SSSSSSSSSSSSS

											Created by HackerHevin""", 'red'))
print(colored("\n================================================================================"))

ip = str(input(colored("[+] IP: ",'green')))
port = str(input(colored("[+] Port: ",'green')))
packet = str(input(colored("[+] Packets: ",'green')))
thread = str(input(colored("[+]: Threads ",'green')))
time.sleep(1.5)

