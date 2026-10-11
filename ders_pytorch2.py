import torch

# 1. Məlumatlarımız (Giriş məlumatı 'x' və məqsədimiz olan 'y')
# Fərz edək ki, düsturumuz y = 3 * x kimidir. Modelin bunu özü tapmasını istəyirik.
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[3.0], [6.0], [9.0], [12.0]])

# 2. Təsadüfi bir çəki (weight) təyin edirik - model bunu dəyişib '3' etməyə çalışacaq
# requires_grad=True o deməkdir ki, kompüter bu rəqəmin səhvini hesablayıb düzəldə bilər.
w = torch.tensor([[1.0]], requires_grad=True)

print(f"Başlanğıcda təsadüfi çəki (w): {w.item()}")

# 3. Öyrənmə dövrü (Training Loop) - 10 dəfə təkrarlayaq
learning_rate = 0.01

for epoch in range(100):
    # Modelin təxmini (Prediksiya)
    y_tahmin = x * w
    
    # Səhv (Loss) - Təxminimizlə gerçək 'y' arasında nə qədər fərq var?
    loss = ((y_tahmin - y) ** 2).mean()
    
    # Səhvi geriyə yayaraq çəkinin hansı tərəfə dəyişməli olduğunu hesablayırıq
    loss.backward()
    
    # Çəmini öyrənmə sürətinə görə yeniləyirik
    with torch.no_grad():
        w -= learning_rate * w.grad
        # Gradiyenti sıfırlayırıq ki, növbəti dövrəyə təsir etməsin
        w.grad.zero_()
        
    print(f"Dövür {epoch+1}: Səhv (Loss) = {loss.item():.4f}, Çəki (w) = {w.item():.4f}")

print(f"\nNəticə: Model uğurla öyrəndi və çəmini tapdı -> w = {w.item():.2f}")