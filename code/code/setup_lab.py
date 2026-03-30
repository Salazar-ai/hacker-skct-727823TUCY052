# Varun V | Roll No: 52
# student_name: Varun V
# roll_number: 52
# project_name: IoT Device Fingerprinter
# date: 2026-03-30

import sys
import subprocess
import datetime
import platform

ROLL_NUMBER = "52"

def ts():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    print(f"Roll No: {ROLL_NUMBER} | {ts()}")
    print(f"[setup_lab.py] OS: {platform.system()} {platform.release()}")
    print(f"[setup_lab.py] Python: {sys.version}")
    major, minor = sys.version_info[:2]
    if (major, minor) < (3, 10):
        print(f"[ERROR] Python 3.10+ required, found {major}.{minor}")
        sys.exit(1)
    print(f"[OK] Python {major}.{minor}")
    for dep in ["rich>=13.0.0"]:
        r = subprocess.run(["uv", "pip", "install", dep], capture_output=True, text=True)
        print(f"  {dep} → {'OK' if r.returncode == 0 else 'WARN'}")
    print(f"[setup_lab.py] Done | Roll No: {ROLL_NUMBER} | {ts()}")

if __name__ == "__main__":
    main()
