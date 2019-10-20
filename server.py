import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 1234))
server.listen(5)
connection_list = [server]
while True:
	read_sockets, _, _ = select.select(connection_list, [], [])
	for socket in read_sockets :
		if socket == server :
			connection, address = server.accept()
			connection_list.append(connection)
			print("Client is connected")
			connection.send(bytes("You are connected", "utf-8"))
		elif socket == connection :
			data = socket.recv(1024)
			if data :
				print(data.decode("utf-8"))
				print('Server > ', end = " ")
				msg = "Server > " + input()
				connection.send(bytes(msg, "utf-8"))