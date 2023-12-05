from joblib import load
from pathlib import Path

__version__ = "1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

path1 = fr"{BASE_DIR}\rfStressLevel.joblib"
path2 = fr"{BASE_DIR}\rfDepression.joblib"

try:
    model1 = load(path1)
    model2 = load(path2)

except FileNotFoundError:
    print(f"Error: Model file not found")
