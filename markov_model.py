# markov_model.py
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def build_markov():
    print("[2/5] Building Markov Transition Matrix...")

    # Load evaluation matrix from previous step
    D = pd.read_csv("results/evaluation_matrix_step1.csv", index_col=0)

    # Ensure all expected criteria are present
    expected = ["ResponseTime", "Cost", "Availability", "Usability", "Flexibility", "Security"]
    for col in expected:
        if col not in D.columns:
            D[col] = 1e-6
            print(f"[WARN] Column '{col}' missing — added filler values.")

    criteria = expected
    n = len(criteria)

    # Convert to numeric matrix
    M = D[criteria].to_numpy(dtype=float)

    # Compute pairwise similarity using correlation as proxy for transition tendencies
    sim = np.corrcoef(M.T)
    sim = np.nan_to_num(sim, nan=1e-3)  # replace NaN correlation with small positive number
    sim = np.maximum(sim, 0)  # negative correlation replaced with 0 (no transition)

    # Build transition matrix P
    P = np.copy(sim)

    # Handle rows that might be all zeros (constant features)
    for i in range(n):
        if np.all(P[i] == 0):
            P[i] = np.ones(n) * (1 / n)

    # Normalize each row so they sum to 1
    row_sums = P.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1e-6
    P = P / row_sums

    # Save matrix
    os.makedirs("results", exist_ok=True)
    np.savetxt("results/transition_matrix.csv", P, delimiter=",", fmt="%.6f")
    print("[INFO] Saved Markov transition matrix → results/transition_matrix.csv")

    # ===============================
    # 📊 Plot Figure 3: Transition Matrix Heatmap
    # ===============================
    plt.figure(figsize=(7, 6))
    im = plt.imshow(P, cmap="Blues", interpolation="nearest", vmin=0, vmax=1)
    plt.title("Figure 3: Transition Probability Matrix")
    plt.xticks(range(n), criteria, rotation=30)
    plt.yticks(range(n), criteria)
    plt.colorbar(im, label="Transition Probability")

    # Annotate each cell with value
    for i in range(n):
        for j in range(n):
            value = P[i, j]
            color = "white" if value > 0.5 else "black"
            plt.text(j, i, f"{value:.2f}", ha="center", va="center", color=color, fontsize=9)

    plt.tight_layout()
    plt.savefig("results/Figure3_Transition_Matrix.png", dpi=300)
    plt.close()
    print("[INFO] Saved Figure 3 → results/Figure3_Transition_Matrix.png")

    print("[✅] Markov model generation complete!\n")

if __name__ == "__main__":
    build_markov()
