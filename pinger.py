#pinger.py - send a ping message to a hostname
#Similar functionality to cmd's ping hostname.

import os
hostname = input("Enter the host name: ")
response = os.system("ping -c 1 " + hostname)

#and then check the response...
