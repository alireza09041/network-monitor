# Network Monitoring Tool

A Python-based network monitoring application that checks the availability of IP addresses and domain names, stores monitoring results in SQLite, and generates uptime reports.

## Features

- Read IP addresses and domain names from a text file.
- Check device availability using the ping command.
- Perform concurrent network checks using ThreadPoolExecutor.
- Store monitoring history in an SQLite database.
- Calculate uptime percentage for each device.
- Display monitoring reports in the terminal.
- Export uptime reports to CSV.
- Handle common errors such as timeouts and invalid addresses.
- Automated tests using pytest.

## Project Structure

```text
network-monitor/
├── main.py
├── pinger.py
├── database.py
├── reports.py
├── devices.txt
├── monitoring.db
├── uptime_report.csv
└── tests/
    └── test_monitor.py
```

## Requirements

- Python 3.10+
- pytest (for running tests)

The application uses Python standard-library modules for its main functionality.

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd network-monitor
```

Install pytest:

```bash
pip install pytest
```

## Configuration

Add the IP addresses or domain names you want to monitor to `devices.txt`.

Example:

```text
8.8.8.8
127.0.0.1
google.com
```

## Run the Application

```bash
python main.py
```

## Run Tests

```bash
pytest -v
```

## Technologies

- Python
- SQLite
- SQL
- ThreadPoolExecutor
- CSV
- pytest

## Limitations

- Ping-based availability does not guarantee that an application or service is working.
- Some devices may block ICMP requests, even when they are online.
- Uptime percentage is calculated from successful checks, not continuous monitoring time.

## Future Improvements

- Add scheduled monitoring.
- Add a graphical dashboard.
- Support monitoring specific ports and services.
- Add logging and notification features.