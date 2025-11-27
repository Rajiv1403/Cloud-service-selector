import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load transition matrix
P = np.loadtxt("results/transition_matrix.csv", delimiter=",")
criteria = ["ResponseTime","Cost","Availability","Usability","Flexibility","Security"]

# Convert to DataFrame
P_df = pd.DataFrame(P, index=criteria, columns=criteria)

# Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(P_df, annot=True, cmap="Blues", fmt=".2f")
plt.title("Transition Probability Matrix (Markov Chain)")
plt.xlabel("Next State (Preference)")
plt.ylabel("Current State (Preference)")
plt.tight_layout()
plt.show()
