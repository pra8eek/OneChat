import select
import sys
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.43.166"
port = 1234
client.connect((host, port))
while True :
	read_sockets, _, _ = select.select([sys.stdin, client], [], [])
	for socket in read_sockets :
		if socket == client :		
			data = client.recv(1024)
			print(data.decode("utf-8"))
			print('Client > ', end = " ")
			msg = 'Client > ' + input()
			client.send(bytes(msg, 'utf-8'))
			