#!/usr/bin/env python3
"""Self-check the Amazon circuit breaker without touching the network."""

import os
import stat
import subprocess
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
MINE = REPO / "tooling" / "scripts" / "niche_mine.sh"


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        research = Path(tmp)
        scout = research / "kdp-scout" / ".venv" / "bin" / "kdp-scout"
        scout.parent.mkdir(parents=True)
        scout.write_text(
            "#!/usr/bin/env bash\n"
            "echo 'Network error querying autocomplete: NameResolutionError Failed to resolve'\n"
            "exit 0\n"
        )
        scout.chmod(scout.stat().st_mode | stat.S_IXUSR)

        run = subprocess.run(
            [str(MINE), "historical fiction", "-m", "us"],
            capture_output=True,
            text=True,
            env={**os.environ, "RTPB_RESEARCH_DIR": str(research)},
        )
        output = run.stdout + run.stderr
        ledger = research / "ledger" / "niche-ledger.csv"

        checks = {
            "network failure exits 3": run.returncode == 3,
            "circuit breaker is reported": "circuit-breaker triggered" in output,
            "cached rows cannot reach the ledger": not ledger.exists(),
        }
        failures = []
        for name, ok in checks.items():
            print(f"{'PASS' if ok else 'FAIL'}  {name}")
            if not ok:
                failures.append(name)

        if failures:
            print(output)
            print(f"{len(failures)} FAILED: {', '.join(failures)}")
            return 1

    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
