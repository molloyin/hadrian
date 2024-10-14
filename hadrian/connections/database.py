import sqlite3
from datetime import datetime
from dataclasses import dataclass

@dataclass 
class database():
    db_path = "/home/pi64/code/hadrian"
    
    def __post_init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def initialize_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS metrics (
                iteration INTEGER PRIMARY KEY,
                action TEXT,
                timestamp TEXT
            )
        ''')
        self.conn.commit()

    def add_metric(self, iteration: int, action: str):
        timestamp = datetime.now().isoformat()  # Get the current timestamp
        self.cursor.execute('''
            INSERT INTO metrics (iteration, action, timestamp)
            VALUES (?, ?, ?)
        ''', (iteration, action, timestamp))
        self.conn.commit()

    def close(self):
        self.conn.close()
