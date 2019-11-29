#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
import select
import errno
import socket
import sys
from threading import Thread
import tkinter

def receive():
	"""Handles receiving of messages."""
	while True :
		try :
			username_header = client.recv(HEADER_LENGTH)
			if not len(username_header) :
				print("Connection closed by server")
				sys.exit()

			username_length = int(username_header.decode("utf-8"))
			username = client.recv(username_length).decode("utf-8")

			message_header = client.recv(HEADER_LENGTH)
			message_length = int(message_header.decode("utf-8"))
			message = client.recv(message_length).decode("utf-8")

			msg_list.configure(state='normal')
			msg_list.insert(tkinter.END, username + " > " + message + "\n")
			msg_list.configure(state='disabled')
			
	
		except IOError as e :
			if e.errno == errno.EAGAIN or e.errno == errno.EWOULDBLOCK :
				continue
			else :
				print("Error : ", str(e))
				sys.exit()

		except Exception as e:
			print("Error: ", str(e))
			sys.exit()
'''
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

'''

def send():
	message = my_msg.get()
	my_msg.set("") 
	if message == "{quit}":
		client.close()
		top.quit()

	msg_list.configure(state='normal')
	msg_list.insert(tkinter.END, my_username + " > " + message + "\n")
	msg_list.configure(state='disabled')
			
	message = message.encode("utf-8")
	message_header =  f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
	client.send(message_header + message )

def on_closing(event=None):
	"""This function is to be called when the window is closed."""
	my_msg.set("{quit}")
	send()


top = tkinter.Tk()
top.title("A gaye batiyane")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.

scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.

msg_list = tkinter.Text(messages_frame, state='disabled', height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand =  True)

msg_list.pack()
msg_list.configure(state='normal')
msg_list.insert(tkinter.END, "Wecome to Hooli Chat! This is the chat-pakoda wali chat. Ok bye\n")
msg_list.configure(state='disabled')

# messages_frame.insert(tkinter.END, "Just a text Widget\nin two lines\n")

top.protocol("WM_DELETE_WINDOW", on_closing)

messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

photo = tkinter.PhotoImage(file = "./send.png") 
tkinter.Button(top, text = 'Send', image = photo)

#----Now comes the sockets part----

HEADER_LENGTH = 10
IP = "192.168.43.166"
PORT = 1234
my_username  = sys.argv[1]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client.send(username_header + username)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.