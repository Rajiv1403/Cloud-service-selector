import numpy as np
import pandas as pd
import os

print("=== evaluation_matrix_step1.csv ===")
D = pd.read_csv("results/evaluation_matrix_step1.csv", index_col=0)
print(D.head())
print("columns:", list(D.columns))
print("any NaN?:", D.isna().any().any())
print("col sums (min,max):", D.sum().min(), D.sum().max())
print()

print("=== transition_matrix.csv (or P_matrix.csv) ===")
try:
    P = np.loadtxt("results/transition_matrix.csv", delimiter=",")
except:
    P = np.loadtxt("results/P_matrix.csv", delimiter=",")
print("shape P:", P.shape)          
print("row sums:", P.sum(axis=1))
print("min,max:", P.min(), P.max())
print(P)
print()

print("=== P_smoothed.csv (if exists) ===")
if os.path.exists("results/P_smoothed.csv"):
    P2 = np.loadtxt("results/P_smoothed.csv", delimiter=",")
    print("shape P_smoothed:", P2.shape)
    print("row sums:", P2.sum(axis=1))
    print("min,max:", P2.min(), P2.max())
    print(P2)
else:
    print("P_smoothed.csv not found")
