# Varun V | Roll No: 52
# student_name: Varun V
# roll_number: 52
# project_name: IoT Device Fingerprinter
# date: 2026-03-30

import sys
import json
import datetime
import argparse
from collections import Counter

ROLL_NUMBER = "52"

def ts():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    print(f"Roll No: {ROLL_NUMBER} | {ts()}")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", default="results.json")
    parser.add_argument("--output", "-o", default="analysis_report.txt")
    args = parser.parse_args()

    try:
        with open(args.input) as f:
            results = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] {args.input} not found — run run_tool.py first")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON: {e}")
        sys.exit(1)

    if isinstance(results, dict):
        flat = [r for tc in results.values() for r in tc]
    else:
        flat = results

    type_c = Counter(r["device_type"] for r in flat)
    vendor_c = Counter(r["vendor"] for r in flat)
    port_c = Counter(p for r in flat for p in r["open_ports"])
    high = sum(1 for r in flat if r["confidence"] == "High")
    medium = sum(1 for r in flat if r["confidence"] == "Medium")
    low = sum(1 for r in flat if r["confidence"] == "Low")

    lines = [
        "="*60,
        "IoT Device Fingerprinter — Analysis Report",
        f"Roll No: {ROLL_NUMBER} | Varun V | {ts()}",
        "="*60,
        f"\nTotal devices : {len(flat)}",
        f"High conf     : {high}",
        f"Medium conf   : {medium}",
        f"Low conf      : {low}",
        "\n--- Device Types ---",
        *[f"  {k:40s}: {v}" for k, v in type_c.most_common()],
        "\n--- Top Vendors ---",
        *[f"  {k:40s}: {v}" for k, v in vendor_c.most_common(5)],
        "\n--- Common Ports ---",
        *[f"  Port {p:5d}: {c}" for p, c in port_c.most_common(10)],
        "\n--- Device Table ---",
        f"  {'IP':15s}  {'Type':32s}  {'Conf':6s}  Vendor",
        "  " + "-"*74,
        *[f"  {r['ip']:15s}  {r['device_type']:32s}  {r['confidence']:6s}  {r['vendor']}" for r in flat],
        "\n" + "="*60,
    ]
    report = "\n".join(lines)
    print(report)
    with open(args.output, "w") as f:
        f.write(report)
    print(f"\n[analyze_results.py] Saved → {args.output} | Roll No: {ROLL_NUMBER} | {ts()}")

if __name__ == "__main__":
    main()
