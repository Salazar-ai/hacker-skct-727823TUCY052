# IoT Device Fingerprinter

**Hacker Techniques — Individual Assignment**
**Roll No:** 52 | **Name:** Varun V | **Category:** Network Reconnaissance
**Institution:** Sri Krishna College of Technology (SKCT)
**GitHub:** https://github.com/Salazar-ai/hacker-skct-727823TUCY052

---

## Tool Summary

A Python-based network reconnaissance tool that discovers, probes, and classifies IoT devices on a local subnet using only the Python standard library — no external dependencies required for core operation.

**Main capability:** Scans a subnet for live hosts, probes 13 common IoT ports concurrently, correlates open ports against a built-in device profile database, and outputs a classified JSON report with confidence scores.

---

## Project Structure

```
hacker-skct-727823TUCY052/
├── code/
│   ├── tool_main.py            # Primary IoT fingerprinter script
│   ├── setup_lab.py            # Pipeline Stage 1: environment setup
│   ├── run_tool.py             # Pipeline Stage 2: tool execution
│   ├── analyze_results.py      # Pipeline Stage 3: result analysis
│   └── helper_modules/
│       ├── banner_grab.py      # Banner grabbing module
│       ├── arp_resolver.py     # MAC/OUI resolution
│       └── port_profiles.py    # IoT device port-profile database
├── notebooks/
│   └── demo.ipynb              # Jupyter demo with sample outputs
├── screenshots/                # Terminal screenshots (TC1, TC2, TC3)
├── report/
│   └── report.pdf              # 2-page assignment report
├── pipeline_52.yml             # Pipeline definition
├── requirements.txt            # Python dependencies (pinned)
├── submission_form.txt         # Submission metadata
└── README.md
```

---

## Lab Environment

| Component | Details |
|-----------|---------|
| OS | Fedora Linux (primary), Kali Linux (VM) |
| Python | 3.10+ |
| VM | VirtualBox with Kali Linux + Metasploitable2 |
| Network | Isolated lab subnet / residential network gateway |
| Folder | `SKCT_52_IoTDeviceFingerprinter/` |

---

## Setup

```bash
git clone https://github.com/Salazar-ai/hacker-skct-727823TUCY052.git
cd hacker-skct-727823TUCY052
pip install -r requirements.txt
```

> Core scanning works with zero dependencies (stdlib only).
> `requirements.txt` covers optional notebook/analysis extras.

---

## Usage

### Single IP scan
```bash
python code/tool_main.py --ip 192.168.1.1
```

### Subnet scan (auto-detect network)
```bash
python code/tool_main.py --subnet 192.168.1.0/24
```

### With banner grabbing + custom output file
```bash
python code/tool_main.py --ip 192.168.1.1 --banner --output results_banner.json
```

### Run full pipeline
```bash
python code/setup_lab.py
python code/run_tool.py
python code/analyze_results.py
```

---

## Test Cases

| TC# | Command | Target | Result |
|-----|---------|--------|--------|
| TC1 | `tool_main.py --ip` | 10.41.2.37 | Ports filtered (campus firewall) |
| TC2 | `run_tool.py` (subnet) | 10.41.2.0/24 | 2 hosts alive, ports filtered |
| TC3 | `tool_main.py --ip --banner` | 10.41.2.37 | Banner mode, separate output file |

---

## Pipeline (`pipeline_52.yml`)

```yaml
project_name: SKCT_52_IoTDeviceFingerprinter
stages:
  - setup
  - run
  - analyze
setup:
  script: python3 setup_lab.py
run:
  script: python3 run_tool.py
analyze:
  script: python3 analyze_results.py
```

---

## Tools Used

- Python 3 (stdlib: `socket`, `subprocess`, `threading`, `json`, `ipaddress`, `datetime`)
- `scapy` (optional — ARP resolution fallback)
- Jupyter Notebook (demo)

---

## Ethical Disclaimer

All scanning was performed exclusively on systems owned by the student or the residential network gateway to which the student's device was connected. No third-party systems were scanned without consent. This tool is for authorised security auditing and educational use only. Complies with Assignment Note #4.
