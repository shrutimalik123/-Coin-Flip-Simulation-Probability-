# Coin Flip Simulation & Probability Analysis

This project simulates coin flips to demonstrate the relationship between empirical probability (observed results) and theoretical probability (calculated using the Binomial distribution).

## Project Overview

The script simulates flipping a fair coin 1000 times. It then:
1.  **Calculates Empirical Probability**: Counts the actual number of heads obtained in the simulation.
2.  **Calculates Theoretical Probability**: Uses the Binomial Probability Mass Function (PMF) to calculate the exact probability of getting a specific number of heads (e.g., exactly 500).

## Installation

To run this project, you need Python installed along with the `numpy` and `scipy` libraries.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd -Coin-Flip-Simulation-Probability-
    ```

2.  **Install dependencies:**
    ```bash
    pip install numpy scipy
    ```

## Usage

Run the simulation script using Python:

```bash
python coin_flip_simulation.py
```

## Simulation Results

Here is an example output from a simulation run:

### Parameters
*   **Total Flips (N):** 1000
*   **Theoretical Probability of Heads (p):** 0.5 (Fair Coin)

### Empirical Results (Simulation)
*   **Number of Heads observed:** 500
*   **Empirical Probability P(Heads):** 0.5000

### Theoretical Probability (Binomial PMF)
*   **Target Outcome:** Exactly 500 Heads
*   **Probability P(X = 500):** ~0.0252 (2.523%)

*Note: The theoretical probability shows that while 500 is the expected value, the chance of getting **exactly** 500 heads in a single trial of 1000 flips is only about 2.5%.*
