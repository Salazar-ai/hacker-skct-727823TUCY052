# student_name: Varun V
# roll_number: 52
# project_name: IoT Device Fingerprinter
# date: 2026-03-30

VENDOR_MAP = {
    "B8:27:EB": "Raspberry Pi Foundation",
    "DC:A6:32": "Raspberry Pi Foundation",
    "E4:5F:01": "Raspberry Pi Foundation",
    "18:FE:34": "Espressif Systems (ESP8266/ESP32)",
    "24:6F:28": "Espressif Systems (ESP8266/ESP32)",
    "30:AE:A4": "Espressif Systems (ESP8266/ESP32)",
    "84:F3:EB": "Espressif Systems (ESP8266/ESP32)",
    "A4:CF:12": "Espressif Systems (ESP8266/ESP32)",
    "10:52:1C": "Belkin International",
    "EC:1A:59": "Belkin International",
    "50:C7:BF": "TP-Link Technologies",
    "B0:BE:76": "TP-Link Technologies",
    "00:17:88": "Philips Hue (Signify)",
    "EC:B5:FA": "Philips Hue (Signify)",
    "7C:49:EB": "Nest Labs (Google)",
    "18:B4:30": "Nest Labs (Google)",
    "44:65:0D": "Amazon (Echo/Ring)",
    "F0:27:2D": "Amazon (Echo/Ring)",
    "68:37:E9": "Amazon (Echo/Ring)",
    "B4:7C:9C": "Wyze Labs",
    "2C:AA:8E": "Wyze Labs",
    "00:1A:22": "Cisco Systems",
    "00:50:56": "VMware (virtual NIC)",
    "08:00:27": "VirtualBox (virtual NIC)",
}

def lookup_vendor(mac):
    if not mac or mac == "N/A":
        return "Unknown"
    oui = ":".join(mac.replace("-", ":").upper().split(":")[:3])
    return VENDOR_MAP.get(oui, "Unknown Vendor")
