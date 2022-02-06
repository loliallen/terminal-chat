import socket
import threading


def handle_user_connection(connection, addr):
    host, port = addr
    while True:
        data = connection.recv(1024)
        if data:
            message = f'{host}: ' + data.decode("utf-8")
            print(f"> {message}")
            connection.send(message.encode())
        else:
            connection.close()
            break


def server():
    sock = socket.socket()
    sock.bind(("localhost", 8080))
    sock.listen(20)

    while True:
        conn, addr = sock.accept()
        host, port = addr
        print(f"New connection from {host}")
        threading.Thread(target=handle_user_connection, args=(conn, addr)).start()


if __name__ == "__main__":
    server()
