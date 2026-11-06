"""Paths for local research inputs and generated figures/tables."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_FILE = Path(os.environ.get('PROJECT_CONFIG', ROOT / 'config.json'))
CONFIG = json.loads(CONFIG_FILE.read_text(encoding='utf-8')) if CONFIG_FILE.is_file() else {}
DATA_DIR = Path(os.environ.get('PROJECT_DATA_DIR', CONFIG.get('data_dir', 'data'))).expanduser()
OUTPUT_DIR = Path(os.environ.get('PROJECT_OUTPUT_DIR', CONFIG.get('output_dir', 'outputs'))).expanduser()
if not DATA_DIR.is_absolute():
    DATA_DIR = ROOT / DATA_DIR
if not OUTPUT_DIR.is_absolute():
    OUTPUT_DIR = ROOT / OUTPUT_DIR
BOOTSTRAP_RESAMPLES = int(os.environ.get('BOOTSTRAP_RESAMPLES', CONFIG.get('bootstrap_resamples', 10000)))
RANDOM_SEED = int(os.environ.get('RANDOM_SEED', CONFIG.get('random_seed', 1)))
if BOOTSTRAP_RESAMPLES < 1000:
    raise ValueError('BOOTSTRAP_RESAMPLES must be at least 1000 for percentile intervals.')

def input_path(name):
    value = Path(name).expanduser()
    path = value if value.is_absolute() else DATA_DIR / value
    if not path.is_file():
        raise FileNotFoundError(f'Required input {name}: {path}. Set PROJECT_DATA_DIR or data_dir in config.json.')
    return path

def output_path(name):
    path = OUTPUT_DIR / name
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

def table_path(name):
    configured = Path(name).expanduser()
    source = configured if configured.is_absolute() else DATA_DIR / configured
    generated = OUTPUT_DIR / 'tables' / name
    if source.is_file():
        return source
    if generated.is_file():
        return generated
    raise FileNotFoundError(f'Required table {name}: provide {source} or generate {generated}.')

def require_columns(frame, names):
    missing = sorted(set(names) - set(frame.columns))
    if missing:
        raise ValueError('Missing input columns: ' + ', '.join(missing))
