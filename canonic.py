import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funzione esponenziale per il fitting
def exp_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Inizializzazione del vettore
canonic = np.full(400,10)

# Numero di iterazioni
num_iterations = 1000000

# Iterazioni per modificare il vettore
for _ in range(num_iterations):
    indexes = random.sample(range(len(canonic)), 2)
    index1, index2 = indexes[0], indexes[1]
    canonic[index1] += 1
    while canonic[index2] == 0:
        index2 = random.choice(range(len(canonic)))
    canonic[index2] -= 1

# Calcolo del valore massimo
max_value = int(max(canonic))

# Creazione dell'istogramma
counts, bins, _ = plt.hist(canonic, bins=max_value, alpha=0.6, color='g', label='Dati')

# Calcolo dei centri dei bin
bin_centers = (bins[:-1] + bins[1:]) / 2

# Fitting esponenziale
popt, pcov = curve_fit(exp_func, bin_centers, counts, p0=(1, 1e-6, 1))

# Creazione dei dati per il fitting
x_fit = np.linspace(0, max_value, 1000)
y_fit = exp_func(x_fit, *popt)

# Stampa del valore massimo
print("Valore massimo:", max_value)

# Plot dell'istogramma e del fitting
plt.plot(x_fit, y_fit, 'r-', label='Fit esponenziale')
plt.title('Simulation of the Canonic Distribution')
plt.xlabel('Valore')
plt.ylabel('Frequenza')
plt.legend()
plt.show()

# Calcolo dell'energia media per particella dopo l'equilibrio
average_energy_per_particle = np.mean(canonic)

# Costante di Boltzmann in J/K
k_B = 1.38e-23

# Confronto del parametro b ottenuto dal fitting con 1/(k_B * T)
fitted_b = popt[1]

# Calcolo della temperatura T
T = 1 / (k_B * fitted_b)

# Calcolo di 1/(k_B * T)
expected_b = 1 / (k_B * T)

print(f"Parametro b ottenuto dal fitting: {fitted_b}")
print(f"Valore atteso di 1/(k_B * T): {expected_b}")
print(f"Temperatura dedotta T: {T} K")

