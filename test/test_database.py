import pytest
from hadrian.connections.database import database

@pytest.fixture
def db(tmp_path):
    db_path = tmp_path / "test_metrics.sqlite"
    db = database(str(db_path))
    db.initialize()
    yield db
    db.close()

def test_add_metric(db):
    db.add_metric(1, "FORWARD", b"dummy_image_data")
    result = db.cursor.execute("SELECT * FROM metrics WHERE iteration = 1").fetchone()
    assert result is not None, "Metric was not inserted into the database"
    assert result[1] == "FORWARD", "Action was not stored correctly"

def test_initialize(db):
    tables = db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    assert ("metrics",) in tables, "Metrics table was not created during initialization"
