
import socket
import threading


def notify_ready(port, message="READY\n", host="127.0.0.1", timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout) as s:
            s.sendall(message.encode("utf-8"))
        return True
    except Exception as e:
        print(f"[Notifier] Failed to notify on port {port}: {e}")
        return False


class ServerReadyListener:

    def __init__(self, port, timeout=5):
        self.port = port
        self.timeout = timeout
        self._message = None
        self._event = threading.Event()
        self._thread = threading.Thread(target=self._listen, daemon=True)
        self._thread.start()

    def _listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", self.port))
            s.listen(1)
            s.settimeout(self.timeout)
            try:
                conn, _ = s.accept()
                with conn:
                    self._message = conn.recv(1024).decode("utf-8", errors="replace").strip()
            except socket.timeout:
                self._message = "[!] Server did not respond with READY in time"
            finally:
                self._event.set()

    def wait(self):
        self._event.wait(self.timeout)
        return self._message or "[!] No response from server"
