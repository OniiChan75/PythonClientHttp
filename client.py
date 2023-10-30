import socket
import json

def read_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print(f"Config file '{file_path}' not found.")
        return None

def send_http_request(host, port, path):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the HTTP server
    server_address = (host, port)
    client_socket.connect(server_address)

    # Create an HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"

    # Send the request to the server
    client_socket.send(request.encode())

    # Receive the response from the server
    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    # Close the socket
    client_socket.close()

    # Print the response
    print(response.decode())

if __name__ == "__main__":
    config = read_config("config.json")
    
    if config:
        host = config.get("host")
        port = config.get("port")
        path = config.get("path")

    send_http_request(host, port, path)

