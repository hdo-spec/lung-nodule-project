import torch

print("CUDA available:", torch.cuda.is_available())
print("GPU 개수:", torch.cuda.device_count())

if torch.cuda.is_available():
    print("현재 GPU:", torch.cuda.get_device_name(0))
    print("현재 GPU 메모리 할당:", torch.cuda.memory_allocated(0))
    print("현재 GPU 메모리 캐시:", torch.cuda.memory_reserved(0))