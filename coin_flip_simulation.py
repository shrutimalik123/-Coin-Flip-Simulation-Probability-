import numpy as np
from scipy.stats import binom
import math

# --- Simulation Parameters ---
# Assume a fair coin (p=0.5)
NUM_FLIPS = 1000
PROB_HEADS_THEORY = 0.5
TARGET_HEADS = 500 # The specific outcome we are interested in for the theoretical calculation

print(f"--- Coin Flip Simulation Parameters ---")
print(f"Total Flips (N): {NUM_FLIPS}")
print(f"Theoretical Probability of Heads (p): {PROB_HEADS_THEORY}")
print("\n" + "="*50 + "\n")


# 1. Empirical Probability Calculation (Simulation)
# ----------------------------------------------------------------------
# np.random.choice([0, 1], ...) simulates flips: 1 = Heads, 0 = Tails
# Size=NUM_FLIPS creates a 1D array of 1000 outcomes.
flips = np.random.choice([0, 1], size=NUM_FLIPS, p=[1 - PROB_HEADS_THEORY, PROB_HEADS_THEORY])

# Calculate the number of heads (summing the '1's)
num_heads_simulated = np.sum(flips)

# Calculate the empirical probability
# Empirical P(Heads) = (Count of Heads) / (Total Flips)
empirical_prob_heads = num_heads_simulated / NUM_FLIPS

print(f"--- Empirical Results (Simulation) ---")
print(f"Number of Heads observed: {num_heads_simulated}")
print(f"Empirical Probability P(Heads): {empirical_prob_heads:.4f}")


# 2. Theoretical Probability Calculation (Binomial Distribution)
# ----------------------------------------------------------------------
# The probability of getting exactly 'k' successes in 'n' independent Bernoulli trials
# is given by the Binomial PMF: P(k; n, p) = C(n, k) * p^k * (1-p)^(n-k)

# Using scipy.stats.binom.pmf to calculate P(X = 500) where N=1000, p=0.5
theoretical_prob_500 = binom.pmf(k=TARGET_HEADS, n=NUM_FLIPS, p=PROB_HEADS_THEORY)

print("\n" + "="*50 + "\n")
print(f"--- Theoretical Probability (Binomial PMF) ---")
print(f"Target Outcome (k): {TARGET_HEADS} Heads")
print(f"P(X = 500 Heads in 1000 Flips): {theoretical_prob_500}")

# Convert the theoretical probability to a percentage for better understanding
print(f"This outcome has a theoretical chance of: {theoretical_prob_500 * 100:.3f}%")
