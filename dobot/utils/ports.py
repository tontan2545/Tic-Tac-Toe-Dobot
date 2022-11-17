import re
from typing import Optional
from serial.tools import list_ports


def get_port(port: Optional[str]) -> str:
    return scan_usb_serial() if port is None else port


def scan_usb_serial() -> str:
    com_ports = list_ports.comports()
    devices = list(filter(lambda x: re.match(r'/dev/cu.usbserial-\w{4}', x.device), com_ports))
    if len(devices) < 1:
        raise Exception('No Dobot found')
    if len(devices) > 1:
        raise Exception(f"Multiple devices found, please select the following: {[x.device for x in devices]}")
    print("Connected to Dobot at", devices[0].device)
    return devices[0].device

