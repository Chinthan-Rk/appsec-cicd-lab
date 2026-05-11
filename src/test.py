import subprocess
from pathlib import Path
from datetime import datetime

TARGET_FILE = "targets.txt"
OUTPUT_DIR = Path("nmap_results")


NMAP_ARGS = [
    "-sV",          # service/version detection
    "-T3",          # moderate timing
    "--top-ports", "100"
]

def run_nmap(target: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = target.replace("/", "_").replace(":", "_")
    output_file = OUTPUT_DIR / f"{safe_name}_{timestamp}.txt"

    command = [
        "nmap",
        *NMAP_ARGS,
        "-oN", str(output_file),
        target
    ]

    print(f"[+] Scanning {target}")
    print(f"    Command: {' '.join(command)}")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode == 0:
            print(f"[+] Finished {target} -> {output_file}")
        else:
            print(f"[!] Nmap returned error for {target}")
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print(f"[!] Scan timed out for {target}")

    except FileNotFoundError:
        print("[!] nmap not found. Install nmap and make sure it is in PATH.")
        exit(1)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    targets_path = Path(TARGET_FILE)

    if not targets_path.exists():
        print(f"[!] {TARGET_FILE} not found.")
        print("Create a targets.txt file with one IP or hostname per line.")
        return

    targets = [
        line.strip()
        for line in targets_path.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

    if not targets:
        print("[!] No targets found.")
        return

    for target in targets:
        run_nmap(target)


if __name__ == "__main__":
    main()