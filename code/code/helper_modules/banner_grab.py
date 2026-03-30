# student_name: Varun V
# roll_number: 52
# project_name: IoT Device Fingerprinter
# date: 2026-03-30

import socket

HTTP_PORTS = {80, 8080, 8443, 443}

def grab_banner(ip, port, timeout=2.0):
    try:
        with socket.create_connection((ip, port), timeout=timeout) as s:
            if port in HTTP_PORTS:
                s.sendall(b"HEAD / HTTP/1.0\r\nHost: " + ip.encode() + b"\r\n\r\n")
            else:
                s.sendall(b"\r\n")
            return s.recv(1024).decode(errors="replace").strip()[:120]
    except Exception as e:
        return f"[no banner: {e}]"
