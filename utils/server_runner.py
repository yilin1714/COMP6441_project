import socket


def run_tcp_server(port: int, handle_request, host: str = "127.0.0.1", max_connections: int = 1, on_ready=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            s.listen(max_connections)
            print(f"[Server] Listening on {host}:{port} ...")

            if on_ready:
                try:
                    on_ready()
                except Exception as e:
                    print(f"[Server] on_ready() callback failed: {e}")

        except Exception as e:
            print(f"[Server] Failed to start on {host}:{port}: {e}")
            return

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"\n[Server] 📡 Connected by {addr}")
                try:
                    data = conn.recv(1024).decode("utf-8", errors="replace")
                    print(f"   Received raw request: {data[:64] + '...' if len(data) > 64 else data}")

                    response = handle_request(data)
                    conn.sendall(response.encode("utf-8"))

                    print(f"   Response to send: {response}")
                    print(f"   Response sent.")
                except Exception as e:
                    print(f"[Server] Error handling request: {e}")
