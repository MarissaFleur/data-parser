# utils.py
import logging
import os
import json
import yaml
from dataclasses import asdict
from typing import Dict, List, Tuple
from pathlib import Path

logger = logging.getLogger(__name__)

def load_json(file_path: str) -> Dict:
    with open(file_path, 'r') as f:
        return json.load(f)

def load_yaml(file_path: str) -> Dict:
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def save_json(data: Dict, file_path: str) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def save_yaml(data: Dict, file_path: str) -> None:
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def convert_to_dict(data: object) -> Dict:
    if isinstance(data, dict):
        return data
    elif isinstance(data, tuple):
        return {k: v for k, v in data}
    elif isinstance(data, list):
        return {i: v for i, v in enumerate(data)}
    elif isinstance(data, object):
        return asdict(data)
    else:
        raise ValueError("Unsupported data type")

def get_file_path(file_name: str, dir_path: str) -> str:
    return os.path.join(dir_path, file_name)

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()

def split_data(data: List, split_ratio: Tuple[float, float]) -> Tuple[List, List]:
    train_len = int(len(data) * split_ratio[0])
    test_len = int(len(data) * split_ratio[1])
    train_data = data[:train_len]
    test_data = data[train_len:train_len + test_len]
    return train_data, test_data