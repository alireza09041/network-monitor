
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pinger import ping_device
from database import Database
from reports import display_uptime_report, export_uptime_csv
import sqlite3

class NetworkMonitor:

    def __init__(self, devices_file):
        self.devices_file = devices_file

    def load_devices(self):
        devices = []

        try:
            with open(self.devices_file, "r", encoding="utf-8") as file:
                for line in file:
                    address = line.strip()

                    if address:
                        devices.append(address)

        except FileNotFoundError:
            print(f"Error: {self.devices_file} was not found.")
            return []

        except PermissionError:
            print(f"Error: Permission denied for {self.devices_file}.")
            return []

        return devices

    def check_device(self, address):
        status = ping_device(address)
        checked_at = datetime.now().isoformat(timespec="seconds")

        return address, status, checked_at


def main():
    monitor = NetworkMonitor("devices.txt")

    devices = monitor.load_devices()

    if not devices:
        print("No devices found. Monitoring stopped.")
        return

    try:
        database = Database("C:/Users/Mr.Momeni/monitoring_test.db")

        with ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(monitor.check_device, devices)

            for address, status, checked_at in results:
                database.save_result(address, status, checked_at)

                print(f"{address} -> {status}")

        report = database.get_uptime_report()

        display_uptime_report(report)

        export_uptime_csv(report)

    except sqlite3.Error as error:
        print(f"Database error: {error}")

if __name__ == "__main__":
    main()
