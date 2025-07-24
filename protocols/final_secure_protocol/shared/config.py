# shared/config.py

import os
import secrets
from collections import defaultdict
from datetime import timedelta

# ========================
# 🔐 Shared Secret Keys
# ========================

# AES-128 Key (16 bytes)
AES_KEY = b"ThisIsA16ByteKey"  # In real systems, store securely

# HMAC Key (for signing messages and tokens)
HMAC_KEY = b"ThisIsASecretHMACKey"

# ========================
# 👤 User Database (Demo Only)
# ========================

# Plaintext passwords hashed using SHA-256 with salt (demo purpose only)
# In production: store salted+hashed values in a secure DB
USER_DB = {
    "alice": "83be402f932226fb4f20e5580ff7bcd79fe3411d008da4be1da75d7e265a7d75",  # "123456" + "SALT"
    "bob": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd64a4f8f3f846f8d86",    # "password" + "SALT"
}

PASSWORD_SALT = "SALT"  # Used when hashing user passwords

# ========================
# 🔑 Token Configuration
# ========================

# Token lifetime in seconds (e.g., 5 minutes)
TOKEN_EXPIRY_SECONDS = 300

# ========================
# 🧾 Nonce Cache (Per-user)
# ========================

# Structure: { username: set of nonces }
NONCE_CACHE = defaultdict(set)

# Limit how many nonces to store per user (for memory control)
NONCE_CACHE_MAX = 100