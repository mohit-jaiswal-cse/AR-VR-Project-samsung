import torch

print("Torch version:",torch.__version__)

cud_available = torch.cuda.is_available()

if cud_available:
    print("Tes")
else:
    print("No")