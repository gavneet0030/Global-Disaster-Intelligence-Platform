from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]

DATASET_DIR = BASE_DIR / "dataset"

MODEL_DIR = BASE_DIR / "models"

REPORT_DIR = BASE_DIR / "reports"

LOG_DIR = BASE_DIR / "logs"

CACHE_DIR = BASE_DIR / "cache"

ARTIFACT_DIR = BASE_DIR / "artifacts"

EXPORT_DIR = BASE_DIR / "exports"