from main import NetworkMonitor
import main
from datetime import datetime
from database import Database

def test_load_devices(tmp_path):

    devices_file = tmp_path / "devices.txt"

    devices_file.write_text(
        "8.8.8.8\n"
        "127.0.0.1\n"
        "\n"
        "google.com\n",
        encoding="utf-8"
    )

    monitor = NetworkMonitor(devices_file)

    devices = monitor.load_devices()

    assert devices == [
        "8.8.8.8",
        "127.0.0.1",
        "google.com"
    ]

def test_check_device(monkeypatch):

    def fake_ping(address):
        return "ONLINE"

    monkeypatch.setattr(main, "ping_device", fake_ping)

    monitor = main.NetworkMonitor("devices.txt")

    address, status, checked_at = monitor.check_device("8.8.8.8")

    assert address == "8.8.8.8"
    assert status == "ONLINE"

    datetime.fromisoformat(checked_at)

from database import Database


def test_database_save_and_report(tmp_path):

    db_file = tmp_path / "test_monitoring.db"

    database = Database(db_file)

    database.save_result(
        "8.8.8.8",
        "ONLINE",
        "2026-11-09T10:00:00"
    )

    database.save_result(
        "8.8.8.8",
        "OFFLINE",
        "2026-11-09T10:01:00"
    )

    database.save_result(
        "8.8.8.8",
        "ONLINE",
        "2026-11-09T10:02:00"
    )

    report = database.get_uptime_report()

    assert report == [
        ("8.8.8.8", 3, 2)
    ]