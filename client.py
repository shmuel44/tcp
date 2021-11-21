import socket
import os

IP = 'localhost' #socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def dow():
    downloadDir = "/home/shmuel/Downloads/tcp_server-master/server_data"
    FORMAT = "utf-8"

    filename = input('Enter your filename: ')
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.send(bytes (filename, FORMAT))
    with open(os.path.join(downloadDir, filename), 'wb') as file_to_write:
        while True:
            data = socket1.recv(2048)
            if not data:
                break
            file_to_write.write(data)
        file_to_write.close()


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
        elif cmd == "UPLOAD":
            path = data[1]

            with open(f"{path}", "r") as f:
                text = f.read()

            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))
        elif cmd == "DOW":
            dow()


    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()
