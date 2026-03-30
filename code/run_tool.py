# Varun V | Roll No: 52
# student_name: Varun V
# roll_number: 52
# project_name: IoT Device Fingerprinter
# date: 2026-03-30

import sys
import os
import subprocess
import datetime
import argparse

ROLL_NUMBER = "52"

def ts():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def detect_network():
    import socket, platform, re, ipaddress
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            self_ip = s.getsockname()[0]
        if platform.system().lower() == "windows":
            out = subprocess.check_output(["route", "print", "0.0.0.0"], text=True)
            m = re.search(r"0\.0\.0\.0\s+0\.0\.0\.0\s+(\S+)", out)
            router = m.group(1) if m else self_ip.rsplit(".", 1)[0] + ".1"
        else:
            out = subprocess.check_output(["ip", "route"], text=True)
            m = re.search(r"default via (\S+)", out)
            router = m.group(1) if m else self_ip.rsplit(".", 1)[0] + ".1"
        subnet = str(ipaddress.ip_interface(f"{self_ip}/24").network)
        return router, subnet
    except Exception:
        return "192.168.1.1", "192.168.1.0/24"

def main():
    print(f"Roll No: {ROLL_NUMBER} | {ts()}")
    router, subnet = detect_network()
    print(f"[run_tool.py] Detected network: {subnet} (router: {router})")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tool = os.path.join(script_dir, "tool_main.py")

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--network", "-n", default=subnet)
    group.add_argument("--ip", "-i")
    parser.add_argument("--banner", "-b", action="store_true")
    parser.add_argument("--output", "-o", default="results.json")
    args = parser.parse_args()

    cmd = [sys.executable, tool]
    cmd += ["--network", args.network] if not args.ip else ["--ip", args.ip]
    if args.banner:
        cmd.append("--banner")
    cmd += ["--output", args.output]

    print(f"[run_tool.py] Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=script_dir)
    print(f"[run_tool.py] Exit: {result.returncode} | Roll No: {ROLL_NUMBER} | {ts()}")
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
