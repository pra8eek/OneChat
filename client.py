import select
import errno
import socket
import sys

HEADER_LENGTH = 10
IP = "192.168.43.166"
PORT = 1234
my_username  = input("Username : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client.send(username_header + username)

while True :
	message = input(my_username + " > ")
	if message :
		message = message.encode("utf-8")
		message_header =  f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
		client.send(message_header + message)

	try :
		while True:
			username_header = client.recv(HEADER_LENGTH)
			if not len(username_header) :
				print("Connection closed by server")
				sys.exit()

			username_length = int(username_header.decode("utf-8"))
			username = client.recv(username_length).decode("utf-8")

			message_header = client.recv(HEADER_LENGTH)
			message_length = int(message_header.decode("utf-8"))
			message = client.recv(message_length).decode("utf-8")

			print(username,">",message)
	
	except IOError as e :
		if e.errno == errno.EAGAIN or e.errno == errno.EWOULDBLOCK :
			continue
		else :
			print("Error : ", str(e))
			sys.exit()

	except Exception as e:
		print("Error: ", str(e))
		sys.exit()