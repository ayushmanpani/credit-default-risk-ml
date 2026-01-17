import numpy as np

def population_stability_index(expected, actual, bins=10):
    expected_perc, _ = np.histogram(expected, bins=bins)
    actual_perc, _ = np.histogram(actual, bins=bins)

    expected_perc = expected_perc / expected_perc.sum()
    actual_perc = actual_perc / actual_perc.sum()

    psi = np.sum(
        (actual_perc - expected_perc) *
        np.log((actual_perc + 1e-6) / (expected_perc + 1e-6))
    )

    return psi
