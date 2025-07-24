def parse_kv_string(data: str) -> dict:
    result = {}
    for item in data.split("&"):
        try:
            if "=" in item:
                key, value = item.split("=", 1)
                result[key] = value
        except Exception:
            continue
    return result
