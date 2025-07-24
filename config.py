# config.py - Shared configuration and constants

# ========== Default Server Settings ==========
DEFAULT_HOST = "127.0.0.1"
DEFAULT_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 3.0  # in seconds

# ========== AES Encryption Settings (For Insecure Demos Only) ==========
AES_KEY = b"thisisasecretkey"     # 16 bytes for AES-128
AES_IV = b"thisisaninitvect"      # 16 bytes IV (static, insecure)

# ========== Teaching UI Flags ==========
SHOW_VERBOSE_LOGS = True

