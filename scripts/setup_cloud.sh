#!/usr/bin/env bash
# 在租的服务器上运行：bash scripts/setup_cloud.sh
# 可选环境变量：
#   MODEL_DIR  模型存放目录，放在数据盘上（AutoDL 通常是 /root/autodl-tmp/models）
#   MODELS     要下载的 ModelScope 模型，空格分隔
set -e
MODEL_DIR=${MODEL_DIR:-$HOME/data/models}
MODELS=${MODELS:-"Qwen/Qwen3-1.7B"}

# 1. 沿用镜像自带的 torch，不重装
python -c "import torch; print('torch', torch.__version__, '| cuda', torch.cuda.is_available())" \
  || { echo "镜像里没有 torch：请先按该机器的 CUDA 版本安装 torch 再运行本脚本"; exit 1; }

# 2. 安装项目
pip install -e ".[dev,hf]"
pip install modelscope

# 3. 下载模型到数据盘（已存在则跳过）
mkdir -p "$MODEL_DIR"
for m in $MODELS; do
  name=${m#*/}
  if [ -d "$MODEL_DIR/$name" ]; then echo "已存在：$MODEL_DIR/$name"; continue; fi
  python -c "from modelscope import snapshot_download; snapshot_download('$m', local_dir='$MODEL_DIR/$name')"
done

# 4. 生成本机路径配置（已存在则不覆盖）
[ -f configs/paths.yaml ] || sed "s#/path/to#$MODEL_DIR#g" configs/paths.example.yaml > configs/paths.yaml
echo "请检查 configs/paths.yaml 里的路径"

# 5. 冒烟测试
pytest -q
