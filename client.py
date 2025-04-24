import socket

HOST = '127.0.0.1'  
PORT = 12345        

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

except ConnectionRefusedError:
    print("Could not connect to the server. Is it running?")
except Exception as e:
    print(f"An error occurred: {e}")
