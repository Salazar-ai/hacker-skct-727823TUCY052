# student_name: Varun V
# roll_number: 52
# project_name: IoT Device Fingerprinter
# date: 2026-03-30

import sys
import socket
import ipaddress
import platform
import subprocess
import json
import re
import datetime
import argparse
import concurrent.futures
from helper_modules.oui_lookup import lookup_vendor
from helper_modules.banner_grab import grab_banner
from helper_modules.port_profiles import IOT_PORT_PROFILES, score_device

ROLL_NUMBER = "52"
COMMON_IOT_PORTS = [21, 22, 23, 80, 443, 554, 1883, 5683, 8080, 8443, 8883, 9100, 49152]

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ping_host(ip):
    try:
        cmd = ["ping", "-n", "1", "-w", "1000", str(ip)] if platform.system().lower() == "windows" else ["ping", "-c", "1", "-W", "1", str(ip)]
        r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
        return r.returncode == 0
    except Exception:
        return False

def get_mac(ip):
    try:
        if platform.system().lower() == "windows":
            out = subprocess.check_output(["arp", "-a", str(ip)], timeout=5).decode()
            match = re.search(r"([0-9a-f]{2}[-:][0-9a-f]{2}[-:][0-9a-f]{2}[-:][0-9a-f]{2}[-:][0-9a-f]{2}[-:][0-9a-f]{2})", out, re.IGNORECASE)
        else:
            out = subprocess.check_output(["arp", "-n", str(ip)], timeout=5).decode()
            match = re.search(r"([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})", out, re.IGNORECASE)
        return match.group(1).replace("-", ":").upper() if match else "N/A"
    except Exception:
        return "N/A"

def scan_port(ip, port, timeout=1.0):
    try:
        with socket.create_connection((str(ip), port), timeout=timeout):
            return True
    except Exception:
        return False

def scan_host(ip, banner=False):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
        futures = {ex.submit(scan_port, ip, p): p for p in COMMON_IOT_PORTS}
        for f, p in futures.items():
            if f.result():
                open_ports.append(p)
    banners = {p: grab_banner(str(ip), p) for p in open_ports} if banner and open_ports else {}
    mac = get_mac(ip)
    device_type, confidence = score_device(open_ports)
    return {
        "ip": str(ip), "mac": mac, "vendor": lookup_vendor(mac),
        "open_ports": open_ports, "device_type": device_type,
        "confidence": confidence, "banners": banners, "timestamp": timestamp()
    }

def scan_network(cidr, banner=False):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError as e:
        print(f"[ERROR] Invalid CIDR: {e}")
        sys.exit(1)
    hosts = list(network.hosts())
    print(f"[*] Pinging {len(hosts)} hosts in {cidr}...")
    alive = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as ex:
        futures = {ex.submit(ping_host, ip): ip for ip in hosts}
        for f, ip in futures.items():
            if f.result():
                alive.append(ip)
    print(f"[*] {len(alive)} host(s) alive. Fingerprinting...")
    results = []
    for ip in alive:
        r = scan_host(ip, banner=banner)
        results.append(r)
        print(f"  {str(ip):15s}  {r['device_type']:25s}  conf={r['confidence']}  ports={r['open_ports']}")
    return results

def print_report(results):
    print("\n" + "="*60)
    print(f"Roll No: 52  |  Timestamp: {timestamp()}")
    print(f"IoT Device Fingerprinter — {len(results)} device(s) found")
    print("="*60)
    for r in results:
        print(f"\n  IP     : {r['ip']}")
        print(f"  MAC    : {r['mac']}")
        print(f"  Vendor : {r['vendor']}")
        print(f"  Type   : {r['device_type']} (confidence: {r['confidence']})")
        print(f"  Ports  : {r['open_ports']}")
        if r.get("banners"):
            for port, b in r["banners"].items():
                print(f"  Banner [{port}]: {b[:80]}")
    print("="*60)

def main():
    print(f"Roll No: 52 | {timestamp()}")
    parser = argparse.ArgumentParser(description="IoT Device Fingerprinter — Roll 52")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--network", "-n", help="CIDR e.g. 192.168.1.0/24")
    group.add_argument("--ip", "-i", help="Single IP")
    parser.add_argument("--banner", "-b", action="store_true")
    parser.add_argument("--output", "-o", default="results.json")
    args = parser.parse_args()
    results = scan_network(args.network, banner=args.banner) if args.network else [scan_host(args.ip, banner=args.banner)]
    print_report(results)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"[*] Saved to {args.output}")

if __name__ == "__main__":
    main()
