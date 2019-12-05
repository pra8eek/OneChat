#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
import select
import errno
import socket
import sys
from threading import Thread
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

borderImageData = '''
    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
'''

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

			if username == "$Server$" :
				msg_list.configure(state='normal')
				msg_list.insert(tkinter.END, message + "\n")
				msg_list.configure(state='disabled')
				continue

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

def send(random = None):
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
top.title("OneChat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.

scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.

msg_list = tkinter.Text(messages_frame, state='disabled', height=15, width=50, yscrollcommand=scrollbar.set, font=('Times New Roman', 16))
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand =  True)

msg_list.pack()
msg_list.configure(state='normal')
msg_list.insert(tkinter.END, "Welcome to OneChat!\n")

msg_list.configure(state='disabled')

# messages_frame.insert(tkinter.END, "Just a text Widget\nin two lines\n")

top.protocol("WM_DELETE_WINDOW", on_closing)

messages_frame.pack()

style = ttk.Style()
borderImage = tkinter.PhotoImage("borderImage", data=borderImageData)
style.element_create("RoundedFrame", "image", borderImage, border=16, sticky="nsew")
style.layout("RoundedFrame",[("RoundedFrame", {"sticky": "nsew"})])
frame1 = ttk.Frame(style="RoundedFrame", padding=10, width = 30)
entry_field = tkinter.Entry(frame1, textvariable=my_msg, borderwidth=0, highlightthickness=0, width=30)
entry_field.pack(fill="both", expand=True)
entry_field.bind("<Return>", send)
frame1.pack(side=tkinter.LEFT, fill="both", expand=True, padx=10, pady=10)

send_button = tkinter.Button(top, text="Send", command=send)
photo = tkinter.PhotoImage(file = "paper-plane.png") 
photo = photo.subsample(15) 
send_button.config(image = photo)
send_button.pack(side=tkinter.RIGHT)

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