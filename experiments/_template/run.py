"""实验模板：只 import minillm 里的模块，不在这里定义零件。"""
import json
from pathlib import Path

OUT = Path(__file__).parent / "results"


def main():
    OUT.mkdir(exist_ok=True)
    summary = {"note": "把关键数字写进 summary.json，大文件放 results/raw/"}
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
