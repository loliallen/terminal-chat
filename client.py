import socket, threading


def handle_server_messages(socket):
    data = socket.recv(1024)
    print(data.decode())


def main(msg, socket):
    socket.send(msg.encode())


if __name__ == "__main__":
    address = ('localhost', 8080)
    sock = socket.socket()
    sock.connect(address)
    threading.Thread(target=handle_server_messages, args=(sock,)).start()
    main(input('Message: '), sock)