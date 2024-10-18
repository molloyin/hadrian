import sqlite3
from datetime import datetime
from dataclasses import dataclass

@dataclass 
class database():
    db_path: str

    def __post_init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def initialize(self):
        self.cursor.execute('''
            DROP TABLE IF EXISTS metrics
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS metrics (
                iteration INTEGER PRIMARY KEY,
                action TEXT,
                timestamp TEXT,
                image BLOB
            )
        ''')
        self.conn.commit()

    def add_metric(self, iteration: int, action: str, image_data: bytes):
        timestamp = datetime.now().isoformat()  # Get the current timestamp
        self.cursor.execute('''
            INSERT INTO metrics (iteration, action, timestamp, image)
            VALUES (?, ?, ?, ?)
        ''', (iteration, action, timestamp, image_data))
        self.conn.commit()

    def close(self):
        self.conn.close()
