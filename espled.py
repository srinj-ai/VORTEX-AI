import socket

ESP_IP = "192.168.29.205"


def control_led(command):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        s.connect((ESP_IP, 80))

        request = (
            f"GET /{command} HTTP/1.1\r\n"
            f"Host: {ESP_IP}\r\n"
            "Connection: close\r\n"
            "\r\n"
        )

        s.sendall(request.encode())

        # Receive response
        response = s.recv(1024)

        print(response.decode(errors="ignore"))

    except Exception as e:
        print("ERROR:", e)

    finally:
        s.close()