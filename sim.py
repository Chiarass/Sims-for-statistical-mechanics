import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione boltzmann_prob
def boltzmann_prob(energy_diff, T):
    return np.exp(-energy_diff / T)

# Parametri della simulazione
N = 10  # Dimensione della griglia
steps = 10000  # Numero di passi della simulazione
T = 1.0  # Temperatura

# Inizializzazione della griglia con valori di energia
grid = np.full((N, N), 10)

# Simulazione del trasferimento di energia
for _ in range(steps):
    x1, y1 = np.random.randint(0, N, 2)
    x2, y2 = np.random.randint(0, N, 2)

    # Evitiamo trasferimenti nella stessa cella
    while (x1, y1) == (x2, y2):
        x2, y2 = np.random.randint(0, N, 2)

    if grid[x1, y1] > 0:  # Evitiamo trasferimenti da celle vuote
        energy_diff = grid[x1, y1] - grid[x2, y2]

        if np.random.rand() < boltzmann_prob(energy_diff, T):
            grid[x1, y1] -= 1
            grid[x2, y2] += 1

# Calcolo delle probabilità
prob = grid / np.sum(grid)

# Creazione del grafico ad isogrammi
plt.contourf(prob, levels=20, cmap="viridis")
plt.colorbar(label="Probability")
plt.show()
