import matplotlib.pyplot as plt

model_names = ["pythia-14m", "pythia-31m", "pythia-70m", "pythia-160m", "pythia-410m", "pythia-1b"]
params_millions = [14, 31, 70, 160, 410, 1000, 1400]  # in millions
avg_losses = [4.6823, 4.2702, 3.8520, 3.5753, 3.4282, 3.2560, 3.2226]

plt.figure(figsize=(6,4))
plt.plot(params_millions, avg_losses, marker='o', linestyle='-', linewidth=2)
plt.title("Average Loss vs Model Size")
plt.xlabel("Model Parameters (Millions)")
plt.ylabel("Average Loss per Token")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
