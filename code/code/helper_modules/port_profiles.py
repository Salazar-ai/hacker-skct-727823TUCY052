# student_name: Varun V
# roll_number: 52
# project_name: IoT Device Fingerprinter
# date: 2026-03-30

IOT_PORT_PROFILES = {
    "IP Camera / NVR":            {"ports": {554, 80, 443, 8080, 8443}, "required": {554},  "weight": 3},
    "MQTT Broker (IoT Hub)":      {"ports": {1883, 8883},               "required": {1883}, "weight": 4},
    "Smart Router / Gateway":     {"ports": {80, 443, 22, 23},          "required": set(),   "weight": 1},
    "Network Printer":            {"ports": {9100, 80, 443},            "required": {9100}, "weight": 3},
    "Telnet Device (Legacy IoT)": {"ports": {23},                       "required": {23},   "weight": 2},
    "CoAP Device":                {"ports": {5683},                     "required": {5683}, "weight": 4},
    "UPnP Device":                {"ports": {49152},                    "required": {49152},"weight": 2},
    "SSH-Enabled IoT (Pi etc.)":  {"ports": {22, 80},                   "required": {22},   "weight": 2},
    "FTP Device":                 {"ports": {21},                       "required": {21},   "weight": 2},
}

def score_device(open_ports):
    port_set = set(open_ports)
    best_type, best_score, best_conf = "Unknown IoT / Generic Device", 0, "Low"
    for dtype, p in IOT_PORT_PROFILES.items():
        if p["required"] and not p["required"].issubset(port_set):
            continue
        matches = len(port_set & p["ports"])
        score = matches * p["weight"]
        if score > best_score:
            best_score = score
            best_type = dtype
            ratio = matches / len(p["ports"]) if p["ports"] else 0
            best_conf = "High" if ratio >= 0.75 else "Medium" if ratio >= 0.4 else "Low"
    return best_type, best_conf
