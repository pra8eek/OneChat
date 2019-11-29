import socket
import select

HEADER_LENGTH = 10 
IP = "192.168.43.166"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', PORT))

server.listen()
connection_list = [server]
clients = {}
print("SERVER HAS STARTED !!!!")

def receive_message(client) :
	try :
		header = client.recv(HEADER_LENGTH)
		if not len(header) :
			return False
		message_len = int(header.decode('utf-8'))
		return {"header" : header,
				"data" : client.recv(message_len)}
	except :
		return False


while True:
	read_sockets, _, _ = select.select(connection_list, [], [])

	for socket in read_sockets :
		if socket == server :
			connection, address = server.accept()
			user = receive_message(connection)
			if user is False :
				continue
			connection_list.append(connection)
			clients[connection] = user
			print(user["data"].decode("utf-8"), " is now connected")
			# connection.send(bytes("You are connected", "utf-8"))

		else :
			message = receive_message(socket)
			if message is False :
				print("Connection closed from ", clients[socket]["data"].decode("utf-8"))
				connection_list.remove(socket)
				del clients[socket]
				continue

			# user = clients[connection]
			print("Message received from ", clients[socket]["data"].decode("utf-8"), ":", message["data"].decode("utf-8"))

			user_data = clients[socket]["data"]
			user_header =  f"{len(user_data.decode('utf-8')):<{HEADER_LENGTH}}".encode('utf-8')

			for client in connection_list :
				if client != socket and client != server:
					client.send(user_header + user_data + message["header"] + message["data"])