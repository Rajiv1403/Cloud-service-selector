import numpy as np
import cvxpy as cp
import pandas as pd
import os
import matplotlib.pyplot as plt

def compute_bwm():
    criteria = ["ResponseTime","Cost","Availability","Usability","Flexibility","Security"]

    # Example user judgments
    best, worst = 2, 5  # Availability = best, Security = worst
    a_Bj = np.array([4, 5, 1, 3, 2, 7])  # Best to others
    a_jW = np.array([5, 7, 3, 4, 2, 1])  # Others to worst

    n = len(criteria)
    w = cp.Variable(n, nonneg=True)
    xi = cp.Variable(nonneg=True)

    constraints = [cp.sum(w) == 1]

    # Linear BWM constraints (no division)
    for j in range(n):
        constraints += [
            a_Bj[j] * w[j] - w[best] <= xi,
            w[best] - a_Bj[j] * w[j] <= xi,
            w[j] - a_jW[j] * w[worst] <= xi,
            a_jW[j] * w[worst] - w[j] <= xi
        ]

    # Solve optimization problem
    prob = cp.Problem(cp.Minimize(xi), constraints)
    prob.solve()

    weights = w.value / np.sum(w.value)
    bwm_weights = dict(zip(criteria, weights))

    os.makedirs("results", exist_ok=True)
    pd.Series(bwm_weights).to_csv("results/bwm_weights.csv")
    print("[INFO] Saved BWM weights → results/bwm_weights.csv")

    # ============================
    # 📊 FIGURE 4: BWM Weight Chart
    # ============================
    plt.figure(figsize=(6,4))
    plt.bar(criteria, weights, color="orange")
    plt.title("Figure 4: BWM-Derived Criteria Weights")
    plt.ylabel("Weight")
    plt.xlabel("QoS Criteria")
    plt.tight_layout()
    plt.savefig("results/Figure4_BWM_Weights.png", dpi=300)
    print("[INFO] Saved Figure 4 → results/Figure4_BWM_Weights.png")
    plt.show()

if __name__ == "__main__":
    compute_bwm()
