from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from urllib.request import urlopen

base = "http://127.0.0.1:8000"
rows = []

for path in ("/health", "/version"):
    started = perf_counter()

    with urlopen(base + path, timeout=5) as response:
        status = response.status
        body = response.read().decode("utf-8").strip()

    ms = round((perf_counter() - started) * 1000, 1)

    rows.append(f"| {path} | {status} | {body} | {ms} ms |")

report = "\n".join([
    "# Pulse API Health Report",
    f"Generated UTC: {datetime.now(timezone.utc).isoformat()}",
    "",
    "| Endpoint | HTTP Status | Response | Latency |",
    "|---|---:|---|---:|",
    *rows,
    ""
])

Path("reports").mkdir(exist_ok=True)

Path("reports/health-report.md").write_text(
    report,
    encoding="utf-8"
)

print(report)
