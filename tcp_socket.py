import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port

# Create a TCP/IP socket (IPv4 and SOCK_STREAM for TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections (backlog of 1 connection)
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    # Accept an incoming connection
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive data from the client (up to 1024 bytes)
            data = conn.recv(1024)
            if not data:
                break  # No more data, exit loop
            # Echo the received data back to the client
            conn.sendall(data)
