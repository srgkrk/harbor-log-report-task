from pathlib import Path
import json


def test_report_exists():
    assert Path("/app/report.json").exists()


def test_report_valid():
    with open("/app/report.json") as f:
        report = json.load(f)

    assert "total_requests" in report
    assert "unique_ips" in report
    assert "top_path" in report
