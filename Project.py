import numpy as np
import matplotlib.pyplot as plt

def gaussian_channel(signal, noise_std):
    """
    Adds white Gaussian noise (AWGN) to a signal,
    specifying the noise standard deviation.

    Parameters:
    -----------
    signal : np.ndarray
        Input signal.
    noise_std : float
        Standard deviation of the Gaussian noise.

    Returns:
    --------
    noisy_signal : np.ndarray
        Signal after passing through the Gaussian channel.
    """
    noise = np.random.normal(0, noise_std, size=signal.shape)
    return signal + noise

# Test signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t)  # 5 Hz sine wave

# Nois Levels
noise_levels = [0.05, 0.2, 0.5]  # low, medium, high noise

# Generation of noisy signals
noisy_signals = [gaussian_channel(signal, std) for std in noise_levels]

# Noisy signal plotting
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

for ax, noisy, std in zip(axes, noisy_signals, noise_levels):
    ax.plot(t, signal, label='Original Signal', linewidth=2, color='black')
    ax.plot(t, noisy, label=f'Noisy Signal σ = {std}', color='red', alpha=0.5)
    ax.set_ylabel('Amplitude')
    ax.set_title(f'Gaussian Channel with Noise σ = {std}')
    ax.legend()
    ax.grid(True)

axes[-1].set_xlabel('Time [s]')
plt.tight_layout()
plt.show()
