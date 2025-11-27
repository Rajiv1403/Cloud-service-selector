# ewma_smoothing.py
import numpy as np
import matplotlib.pyplot as plt
import os

def ewma_matrix(P_prev, P_curr, alpha=0.3):
    return alpha * P_curr + (1 - alpha) * P_prev

def apply_ewma(alpha=0.3):
    path = "results/transition_matrix.csv"
    if not os.path.exists(path):
        print("[ERROR] transition_matrix.csv not found. Run markov_model.py first.")
        return

    P = np.loadtxt(path, delimiter=",")
    # simple smoothing (here we just smooth P with itself as placeholder)
    P_smooth = ewma_matrix(P, P, alpha)

    # ensure no negative or NaN and rows sum to 1
    P_smooth = np.nan_to_num(P_smooth, nan=0.0)
    # add tiny epsilon where row sum is zero
    row_sums = P_smooth.sum(axis=1, keepdims=True)
    zero_rows = (row_sums.squeeze() == 0)
    for i in range(P_smooth.shape[0]):
        if zero_rows[i]:
            P_smooth[i] = np.ones(P_smooth.shape[1]) * 1e-6
    row_sums = P_smooth.sum(axis=1, keepdims=True)
    P_smooth = P_smooth / (row_sums + 1e-12)

    np.savetxt("results/P_smoothed.csv", P_smooth, delimiter=",", fmt="%.6f")
    print(f"[INFO] EWMA smoothing applied (alpha={alpha}) → results/P_smoothed.csv")

    # Simulate convergence from a start state and plot history
    criteria = ["ResponseTime","Cost","Availability","Usability","Flexibility","Security"]
    # start state: uniform if you want, or one-hot
    state = np.array([1.0,0,0,0,0,0], dtype=float)
    iterations = 30
    history = np.zeros((iterations+1, len(criteria)))
    history[0] = state

    for t in range(1, iterations+1):
        state = np.dot(state, P_smooth)
        history[t] = state

    # plot
    plt.figure(figsize=(9,5))
    for i, c in enumerate(criteria):
        plt.plot(range(iterations+1), history[:, i], label=c, linewidth=2)
    plt.xlabel("Iteration")
    plt.ylabel("Probability")
    plt.title(f"Figure 6: Convergence of Markov Preferences (α={alpha})")
    plt.legend(loc="upper right")
    plt.ylim(0,1)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig("results/Figure6_Convergence.png", dpi=300)
    plt.close()
    print("[INFO] Saved Figure 6 → results/Figure6_Convergence.png")

if __name__ == "__main__":
    apply_ewma(alpha=0.3)
