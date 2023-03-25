import socket
import time

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set server address and port
server_address = ('localhost', 8080)

# set initial data buffer size
data_size = 128

# connect to server
sock.connect(server_address)

while True:
    # create data buffer of current size
    data = b'0' * data_size

    # start timer
    start_time = time.time()

    # send and receive packets to/from server
    for i in range(1000):
        sock.sendall(data)
        sock.recv(data_size)

    # stop timer
    end_time = time.time()

    # calculate speed
    speed = 1000 * data_size / (end_time - start_time) / 1000 / 1000

    # print speed in Mbps
    print(f"Speed: {speed:.2f} Mbps (buffer size: {data_size} bytes)")

    # double buffer size, up to a maximum of 4096 bytes
    data_size = min(data_size * 2, 65536 )

    # wait for 1 second before starting a new test
    time.sleep(1)