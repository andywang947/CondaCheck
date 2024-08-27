import torch

# 確認 PyTorch 是否可以檢測到 GPU
if torch.cuda.is_available():
    print(f"CUDA is available. PyTorch is using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. PyTorch is using CPU.")
