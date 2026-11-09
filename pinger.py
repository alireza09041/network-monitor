
import platform
import subprocess
import ipaddress
import re


def is_valid_domain(address):
    pattern = r"^(?=.{1,253}$)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}$"

    return re.fullmatch(pattern, address) is not None

def ping_device(address):
    address = address.strip()

    if not address:
        return "INVALID_ADDRESS"

    try:
        ipaddress.ip_address(address)

    except ValueError:
        if not is_valid_domain(address):
            return "INVALID_ADDRESS"

    system = platform.system()

    if system == "Windows":
        command = ["ping", "-n", "1", "-w", "1000", address]

    elif system == "Linux":
        command = ["ping", "-c", "1", "-W", "1", address]

    else:
        return "UNSUPPORTED_SYSTEM"

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=3
        )

        if result.returncode == 0:
            return "ONLINE"

        return "OFFLINE"

    except subprocess.TimeoutExpired:
        return "OFFLINE"

    except FileNotFoundError:
        return "PING_COMMAND_NOT_FOUND"
    
    except OSError:
        return "PING_ERROR"
