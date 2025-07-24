import socket


def run_tcp_attack(host: str, port: int, plain_text: str, payload: str, buffer_size: int = 1024, timeout: float = 3.0,
                   verbose: bool = False) -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            if verbose:
                print(f"\n[Attacker] ❗ Connection established")
                print(f"   Server: {host}:{port}")
                print(f"   Plaintext: {plain_text}")
                print(f"   Payload to send: {payload[:64] + '...' if len(payload) > 64 else payload}")
            s.sendall(payload.encode("utf-8"))

            if verbose:
                print(f"   Request sent.")

            response = s.recv(buffer_size).decode("utf-8", errors="replace")
            if verbose:
                print(f"\n[Attacker] 📥 Response received")
                print(f"   Response: {response}")
            return response
    except Exception as e:
        print(f"[Attacker] Error: {e}")
        return ""
