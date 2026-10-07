"""测试分级：
- 默认只跑不依赖大模型的测试（numpy / 小张量），笔记本和 CI 上都能跑；
- 标了 @pytest.mark.torch 的测试，没装 torch 时自动跳过；
- 标了 @pytest.mark.hf 的测试（要加载 Qwen3 等权重），只有设置 RUN_HF=1 时才跑；
- 标了 @pytest.mark.cloud 的测试（超出笔记本能力），只有设置 RUN_CLOUD=1 时才跑。
"""
import importlib.util
import os

import pytest


def pytest_collection_modifyitems(config, items):
    has_torch = importlib.util.find_spec("torch") is not None
    run_hf = os.environ.get("RUN_HF") == "1"
    run_cloud = os.environ.get("RUN_CLOUD") == "1"
    for item in items:
        if "torch" in item.keywords and not has_torch:
            item.add_marker(pytest.mark.skip(reason="未安装 torch"))
        if "hf" in item.keywords and not run_hf:
            item.add_marker(pytest.mark.skip(reason="需要 RUN_HF=1"))
        if "cloud" in item.keywords and not run_cloud:
            item.add_marker(pytest.mark.skip(reason="需要 RUN_CLOUD=1（在租的服务器上跑）"))
