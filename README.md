# IoT Device Fingerprinter

**Roll No:** 52 | **Student:** Varun V
**Category:** Network Reconnaissance / IoT Security
**Institution:** Sri Krishna College of Technology

## What This Tool Does

Scans a network or single IP to identify IoT devices by probing common IoT ports,
grabbing service banners, resolving MAC vendor (OUI lookup), and classifying device
type using a port-profile scoring system.

**Main capability:** Fingerprints IoT devices on a local network by correlating open
ports, MAC vendor OUI data, and service banners to classify device type with confidence.

## Setup

```bash
git clone https://github.com/[YOUR_USERNAME]/hacker-skct-52
cd hacker-skct-52
python scaffold.py        # generates project structure
uv pip install -r SKCT_52_IoTDeviceFingerprinter/requirements.txt
```

## Usage

```bash
cd SKCT_52_IoTDeviceFingerprinter

# Stage 1 — setup
python code/setup_lab.py

# Stage 2 — run (auto-detects your network)
python code/run_tool.py

# Stage 3 — analyze
python code/analyze_results.py --input results.json

# Or run directly
python code/tool_main.py --network 192.168.1.0/24 --banner
python code/tool_main.py --ip 192.168.1.1
```

## Tools Used

Python stdlib only: `socket`, `ipaddress`, `subprocess`, `concurrent.futures`, `re`, `json`

## Lab Environment

- OS: Fedora Linux (host)
- Python: 3.13+, package manager: uv

## Ethical Considerations

All scans performed only on systems owned by the student or with explicit permission.
No testing on public networks. Compliant with Assignment Note #4.
