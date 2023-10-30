#client tcp connect to HTTP server
import socket

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
    host = "192.168.1.90"  # Replace with the host of the HTTP server you want to connect to
    port = 80  # Default HTTP port
    path = "/"  # Request path

    send_http_request(host, port, path)
