import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def rank_services():
    # Load evaluation matrix
    D = pd.read_csv("results/evaluation_matrix_step1.csv", index_col=0)
    # Load weights
    w_bwm = pd.read_csv("results/bwm_weights.csv", index_col=0, header=None).squeeze().dropna().values
    # Load smoothed transition matrix
    if os.path.exists("results/P_smoothed.csv"):
        P_smooth = np.loadtxt("results/P_smoothed.csv", delimiter=",")
    else:
        print("[WARN] P_smoothed.csv not found — using identity matrix.")
        P_smooth = np.eye(len(w_bwm))

    # Compute steady-state preference probabilities
    p = P_smooth.mean(axis=0)

    # Align shapes
    n = min(len(w_bwm), len(p))
    w_bwm, p = w_bwm[:n], p[:n]

    # Dynamic combined weights
    dynamic_weights = 0.7*w_bwm + 0.3*p
    dynamic_weights /= dynamic_weights.sum()

    # Weighted sum model for ranking
    scores = D.iloc[:, :n].dot(dynamic_weights)
    ranking = scores.sort_values(ascending=False)
    os.makedirs("results", exist_ok=True)
    ranking.to_csv("results/final_ranking.csv")
    print("[INFO] Saved final ranking → results/final_ranking.csv")

    # FIGURE 5: Final Cloud Service Ranking
    plt.figure(figsize=(8,5))
    ranking.plot(kind="bar", color="seagreen")
    plt.title("Figure 5: Final Cloud Service Ranking")
    plt.ylabel("Aggregated Score")
    plt.xlabel("Service ID")
    plt.tight_layout()
    plt.savefig("results/Figure5_Final_Ranking.png", dpi=300)
    plt.close()
    print("[INFO] Saved Figure 5 → results/Figure5_Final_Ranking.png")

if __name__ == "__main__":
    rank_services()
