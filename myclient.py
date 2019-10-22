import select
import sys
import socket
import tkinter

top=tkinter.Tk()
top.title("Chat App using Socket Programming")

def send():	
	while True :
		read_sockets, _, _ = select.select([sys.stdin, client], [], [])
		for socket in read_sockets :
			if socket == client :		
				data = client.recv(1024)
				print(data.decode("utf-8"))
				# print('Client > ', end = " ")
				# msg = 'Client > ' + input()
				client.send(bytes(msg, 'utf-8'))
		if data=="{quit}":
			client_socket.close()
			top.quit()

def on_closing():
	msg.set="{quit}"
	send()

messages_frame=tkinter.Frame(top)
msg=tkinter.StringVar()
scrollbar=tkinter.Scrollbar(messages_frame)
msg_list=tkinter.Listbox(messages_frame,height=30,width=50,yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field=tkinter.Entry(top,textvariable=msg)
entry_field.bind("Return",send)
entry_field.pack()
send_button=tkinter.Button(top,text="Send",command=send)
send_button.pack()
top.protocol("WM_DELETE_WINDOW",on_closing)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.43.166"
port = 1234
client.connect((host, port))

top.mainloop()