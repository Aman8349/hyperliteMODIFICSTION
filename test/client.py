import socket

def Main():
    host = '127.0.0.1'  #of server
    port = 4444

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ")

    while True:
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(data)
        print("-"*30)
        if message.lower() == 'exit':
            break
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()