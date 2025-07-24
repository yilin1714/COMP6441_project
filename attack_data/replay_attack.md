# 🔹 Replay Attack

## 📖 Description:
A replay attack occurs when an attacker captures a valid message or transaction and replays it to the server to trick it into executing the same operation again. This attack is especially dangerous in financial systems or authorization flows, where duplicate requests can result in repeated actions like money transfers or access grants.

## 🧪 Attack Scenario / Use Case:
Imagine a bank transfer system where a request like `transfer(from=alice, to=bob, amount=100)` is sent over the network.
If the system does not verify the uniqueness of each request, an attacker can intercept and resend the same request multiple times, causing money to be transferred repeatedly without proper authorization.

## 🔬 How It Works:

1. The attacker captures a legitimate request using tools like Wireshark or by acting as a proxy.
2. The attacker stores and replays the exact same request (e.g., via a crafted TCP connection).
3. The server, lacking nonce or session validation, processes the request again as if it were new.
4. As a result, the same operation is executed multiple times.

## 🛡 Mitigation:
To prevent replay attacks, the protocol should incorporate a nonce (a number used once) or timestamp in each request.
The server must validate that the nonce has not been used before. This ensures each request is unique and cannot be replayed later. 

