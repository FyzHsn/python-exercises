import socket

from decorator_example import LogSocket


def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 2401))
    server.listen(1)
    try:
        while True:
            client, addr = server.accept()
            respond(client)

    finally:
        server.close()