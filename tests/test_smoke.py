"""第 0 步：确认包能被 import、测试框架能跑。之后每章的测试照这个样子往下加。"""
import numpy as np
import pytest

import minillm


def test_import():
    assert minillm.__version__


def test_numpy_works():
    x = np.arange(6).reshape(2, 3)
    assert x.sum() == 15


@pytest.mark.torch
def test_torch_works():
    import torch

    assert torch.ones(2, 3).sum().item() == 6
