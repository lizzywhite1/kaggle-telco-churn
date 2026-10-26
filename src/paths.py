from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ON_KAGGLE = Path("/kaggle/input").exists()

DATA = Path("/kaggle/input/<dataset-name>") if ON_KAGGLE else ROOT / "data/raw"
DB = ":memory:" if ON_KAGGLE else str(ROOT / "db/telco.duckdb")
