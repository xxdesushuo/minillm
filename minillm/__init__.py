"""minillm：《模型算法》配套代码。

scratch/     numpy 从零实现，手写反向（第1、4、14章）
core/        PyTorch 模型零件，最终加载真实权重（第2～4、11～17章）
objectives/  训练目标：MLM 掩码、Loss Mask、DPO、GRPO、奖励函数（第5～8章）
calc/        记账：参数量、KV Cache、FLOPs、roofline、RoPE 波长（第2、4、7、9、11～15章）
utils/       加载模型、hook、计时、画图、评测对比
"""
__version__ = "0.0.1"
