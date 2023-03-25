import socket

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(1)

while True:
    try:
        # wait for a client to connect
        conn, addr = sock.accept()

        # log client address and port
        print(f"New connection from {addr[0]}:{addr[1]}")

        # receive data from client and send it back
        while True:
            data = conn.recv(65536)
            if not data:
                break
            conn.sendall(data)

        # close connection and log
        conn.close()
        print(f"Connection closed by {addr[0]}:{addr[1]}")

    except socket.error:
        # client disconnected, continue listening for new connections
        pass
