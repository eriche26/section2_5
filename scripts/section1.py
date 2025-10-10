#!/usr/bin/env python3

# add import and helper functions here
import numpy as pd

if __name__ == "__main__":
    pd.random.seed(42)
    A = pd.random.normal(size=(4, 4))
    B = pd.random.normal(size=(4, 2))

    print(A @ B)