import socket

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 2401))
    print("Recieved: {0}".format(client.recv(1024)))
    client.close()