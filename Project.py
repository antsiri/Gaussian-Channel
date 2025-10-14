import numpy as np
import matplotlib.pyplot as plt

# Parametri
N = 1000              # numero di campioni
snr_db = 10           # rapporto segnale-rumore in dB

# Segnale di esempio (BPSK)
x = np.random.choice([-1, 1], size=N)

# Calcolo della potenza del segnale
signal_power = np.mean(np.abs(x)**2)

# Conversione SNR da dB a valore lineare
snr_linear = 10**(snr_db/10)

# Varianza del rumore
noise_variance = signal_power / snr_linear

# Generazione del rumore gaussiano
noise = np.sqrt(noise_variance/2) * np.random.randn(N)

# Segnale ricevuto (attraverso il canale AWGN)
y = x + noise

# Plot
plt.figure(figsize=(10,5))
plt.plot(y[:50], 'o-', label="Segnale ricevuto")
plt.plot(x[:50], 's-', label="Segnale trasmesso")
plt.legend()
plt.title("Simulazione Canale AWGN")
plt.xlabel("Campioni")
plt.grid()
plt.show()
