import socket


def run_tcp_client(host: str, port: int, plain_text: str, message: str, buffer_size: int = 1024, timeout: float = 3.0,
                   verbose: bool = False) -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            if verbose:
                print(f"\n[Client] 🚀 Connection established")
                print(f"   Server: {host}:{port}")
                print(f"   Plaintext: {plain_text}")
                print(f"   Payload to send: {message[:64] + '...' if len(message) > 64 else message}")
            s.sendall(message.encode("utf-8"))

            if verbose:
                print(f"   Request sent.")

            response = s.recv(buffer_size).decode("utf-8", errors="replace")
            if verbose:
                print(f"\n[Client] 📥 Response received")
                print(f"   Response: {response}")
            return response
    except Exception as e:
        print(f"[Client] Error: {e}")
        return ""
