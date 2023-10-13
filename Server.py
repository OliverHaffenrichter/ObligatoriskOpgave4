import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        request = data.decode("utf-8")
        response = process_request(request)
        client_socket.send(response.encode("utf-8"))

    client_socket.close()

def process_request(request):
    request_parts = request.split()
    if len(request_parts) != 3:
        return "Invalid request. Please provide 3 values."

    function, num1, num2 = request_parts
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid numbers. Please provide valid numeric values."

    if function == "Random":
        import random
        return str(random.uniform(num1, num2))
    elif function == "Add":
        return str(num1 + num2)
    elif function == "Subtract":
        return str(num1 - num2)
    else:
        return "Invalid function. Please provide 'Random', 'Add', or 'Subtract'."

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.0.160", 12007))
    server.listen(5)

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
