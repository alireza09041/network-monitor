
import sqlite3
from datetime import datetime
from contextlib import closing

class Database:

    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS monitoring_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device TEXT NOT NULL,
                    status TEXT NOT NULL,
                    checked_at TEXT NOT NULL
                )
            """)

    def save_result(self, device, status, checked_at):
        with closing(sqlite3.connect(self.db_name)) as connection:
            with connection:
                connection.execute(
                    """
                    INSERT INTO monitoring_logs (device, status, checked_at)
                    VALUES (?, ?, ?)
                    """,
                    (device, status, checked_at)
                )

    def get_uptime_report(self):
        with closing(sqlite3.connect(self.db_name)) as connection:
            with connection:
                cursor = connection.execute(
                    """
                    SELECT
                        device,
                        COUNT(*) AS total_checks,
                        SUM(
                            CASE
                                WHEN status = 'ONLINE' THEN 1
                                ELSE 0
                            END
                        ) AS online_checks
                    FROM monitoring_logs
                    GROUP BY device
                    ORDER BY device
                    """
                )

                return cursor.fetchall()