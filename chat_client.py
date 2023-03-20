import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = b'This is a request.'
    sock.sendall(message)
    sock.settimeout(3)
    try:
        while True:
            data = str(sock.recv(32))
            if data:
                print('Server response:' + data)
            else:
                break

    except(TimeoutError):
        print('Socket timeout')

finally:
    print('Socket closing')
    sock.close()
