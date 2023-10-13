import socket

def main():
    server_ip = "192.168.0.160"
    server_port = 12007

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    for _ in range(3):
        function = input("Enter function (Random, Add, or Subtract): ")
        num1 = input("Enter number 1: ")
        num2 = input("Enter number 2: ")

        request = f"{function} {num1} {num2}"
        client.send(request.encode("utf-8"))

        response = client.recv(1024)
        print(f"Server Response: {response.decode('utf-8')}")

    client.close()

if __name__ == "__main__":
    main()