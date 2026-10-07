"""读取本机路径配置（configs/paths.yaml）。"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_paths(path: str | Path | None = None) -> dict:
    p = Path(path) if path else ROOT / "configs" / "paths.yaml"
    if not p.exists():
        raise FileNotFoundError(
            f"找不到 {p}。请复制 configs/paths.example.yaml 为 configs/paths.yaml 并填入本机路径。"
        )
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f)
