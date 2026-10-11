import torch

# 1. Sadə bir PyTorch Tensor-u yaradırıq
tensor_verilen = torch.tensor([[1, 2], [3, 4]])

print("--- PyTorch Tensor-umuz ---")
print(tensor_verilen)
print("Tensor-un məlumat tipi:", tensor_verilen.dtype)
print("Tensor-un forması (Shape):", tensor_verilen.shape)

# 2. Riyazi əməliyyatlar
tensor_iki = tensor_verilen * 2
print("\n--- Tensor-un 2-yə vurulmuş halı ---")
print(tensor_iki)

# 3. Sıfırlardan və ya 1-lərdən ibarət xüsusi tensorlar yaratmaq
sifirlar = torch.zeros(2, 3) # 2 sətir, 3 sütunlu sıfır matrisi
print("\n--- Sıfır Tensoru ---")
print(sifirlar)