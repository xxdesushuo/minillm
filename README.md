# minillm

《模型算法》系列文章的配套代码。三种代码各有位置：

- **记账** → `minillm/calc/`：参数量、KV Cache、FLOPs、带宽上限等
- **写零件** → `minillm/scratch/`（numpy 手写反向）、`minillm/core/`（PyTorch 模块）、`minillm/objectives/`（训练目标）
- **跑实验** → `experiments/`、`llamacpp/`

硬件：笔记本（RTX 4060 8G）为主；超出能力的实验和测试标 `cloud`，到租的服务器上跑（`bash scripts/setup_cloud.sh`）。

## 规则

1. 实验只 import，不定义零件。
2. 每个零件一条对齐测试，每个账一条已知答案测试。
3. 每个实验一个 README：问题、做法、结果、结论。
4. 每章结束打 tag：`chXX-done`。

## 安装

```bash
# 1. 先按平台装 torch（笔记本和云服务器的 CUDA 版本各不相同，云镜像多数已自带）
# 2. 再装本项目
pip install -e ".[dev,viz]"
cp configs/paths.example.yaml configs/paths.yaml   # 填本机模型路径
pytest                                             # 默认跳过需要大模型的测试
RUN_HF=1 pytest                                    # 连同加载 HF 模型的测试一起跑
RUN_HF=1 RUN_CLOUD=1 pytest                        # 在租的服务器上跑全部测试
```

## 章节索引

| 章 | 新增模块 | 实验 | tag |
| --- | --- | --- | --- |
| 1 深度学习基础 |  |  |  |
| 2 表示学习 |  |  |  |
| 3 RNN 到 Attention |  |  |  |
| 4 Transformer |  |  |  |
| 5 预训练语言模型 |  |  |  |
