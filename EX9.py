import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "0.0.0.0" 
port = 8080

server_socket.bind((host, port))

server_socket.listen(1)
print(f"Listening for connections on {host}:{port}...")

connection, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

try:
    while True:
        data = connection.recv(1024).decode('utf-8')
        if data:
            print(f"Received data: {data}")
            response = "Hello from Raspberry pi"
            connection.send(response.encode('utf-8'))

except KeyboardInterrupt:
    print("Server closed")

finally:
    connection.close()
    print("Connection closed")
