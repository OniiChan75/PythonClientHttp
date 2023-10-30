# PythonClientHttp
This is a simple Python TCP socket client that connects to an HTTP server and sends an HTTP GET request. You can customize the host, port, and request path by modifying the configuration file `config.json`.

## Prerequisites

- Python 3.x
- A properly configured `config.json` file (see below)

## Usage

1. Clone this repository or download the `client.py` and `config.json` files.

2. Update the `config.json` file to specify the host, port, and request path for the HTTP server you want to connect to. If you don't have a specific configuration, you can use the default values provided.

```json
{
    "host": "your_http_server_ip_or_domain",
    "port": 80,  "Default HTTP port"
    "path": "/your_request_path"
}
```

Run the client.py script to connect to the server and retrieve the HTTP response.

```bash
python client.py
```

The script will read the configuration from config.json and send an HTTP GET request to the specified server. It will then print the response received from the server.