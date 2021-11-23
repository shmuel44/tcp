import socket
import os
import sys



print("Server is starting")
ADDR = ("127.0.0.1", 12345)
SIZE = 1024
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()
print(f"Server is listening.")



def upload():

    print("chek point 1 connect to upload poun")
    f = open("bbb",'wb')
    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        print ("Receiving...")
        l = c.recv(1024)
        while (l):
            print ("Receiving...")
            f.write(l)
            l = c.recv(1024)
        f.close()
        print ("Done Receiving")
        c.send(b'Thank you for connecting')
        c.close()                # Close the connection


def main():
    upload()


if __name__=="__main__":
    main()


