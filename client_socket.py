import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    # Send a message to the server
    client_socket.sendall(b'Hello, server!')
    # Wait to receive data from the server
    data = client_socket.recv(1024)

print(f"Received from server: {data.decode()}")
