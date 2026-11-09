import csv


def display_uptime_report(report):

    print("\nNetwork Monitoring Report")
    print("-" * 40)

    for device, total_checks, online_checks in report:

        if total_checks == 0:
            uptime = 0
        else:
            uptime = (online_checks / total_checks) * 100

        print(
            f"{device:<20} "
            f"Uptime: {uptime:.2f}% "
            f"({online_checks}/{total_checks})"
        )

def export_uptime_csv(report, filename="uptime_report.csv"):

    try:
        with open(filename, "w", newline="", encoding="utf-8-sig") as file:

            fieldnames = [
                "device",
                "total_checks",
                "online_checks",
                "uptime_percent"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for device, total_checks, online_checks in report:

                if total_checks == 0:
                    uptime = 0
                else:
                    uptime = (online_checks / total_checks) * 100

                writer.writerow({
                    "device": device,
                    "total_checks": total_checks,
                    "online_checks": online_checks,
                    "uptime_percent": round(uptime, 2)
                })

        print(f"CSV report saved: {filename}")

    except OSError as error:
        print(f"Error while creating CSV report: {error}")