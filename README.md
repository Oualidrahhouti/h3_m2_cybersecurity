# Simple Python Socket Example

This repository demonstrates a basic socket programming example in Python. It includes an echo server and a client that sends a message and receives an echo.

## Overview

The **server** uses a TCP socket to listen for incoming connections on `127.0.0.1:65432`. When a client connects and sends data, the server echoes the data back. The **client** connects to the server, sends a message, and displays the echoed response.

## Files

- **tcp_socket.py:**  
  Contains the code for the echo server.

- **client_socket.py:**  
  Contains the code for the client that communicates with the server.

## Running the Example

First, ensure you have Python 3 installed. Open a terminal and navigate to the project directory.

### Start the Server

In the terminal, run:

```bash
python tcp_socket.py
```
The server will output:


Server listening on 127.0.0.1:65432
It is now waiting for a connection from a client.

Run the Client
Open a new terminal window (keeping the server running) and navigate to the project directory. Run:
```
python client_socket.py
```
You should see output similar to:

Received from server: Hello, server!
Meanwhile, the server terminal will indicate that it has connected to a client.
