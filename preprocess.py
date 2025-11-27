import pandas as pd
import numpy as np
import os

def preprocess():
    
    df = pd.read_csv(os.path.join("src", "Data-Set-Azu-2018.csv"))


    df = df.rename(columns={
        "Resp. Time": "ResponseTime",
        "Cost": "Cost",
        "Availability": "Availability",
        "Usability": "Usability",
        "Flexibility": "Flexibility",
        "Security": "Security"
    })

    df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors="ignore")

    eps = 1e-9
    df["RT_inv"] = 1.0 / (df["ResponseTime"] + eps)
    df["Cost_inv"] = 1.0 / (df["Cost"] + eps)

    D = pd.DataFrame({
        "ResponseTime": df["RT_inv"],
        "Cost": df["Cost_inv"],
        "Availability": df["Availability"],
        "Usability": df["Usability"],
        "Flexibility": df["Flexibility"],
        "Security": df["Security"]
    })
    D.index = [f"S{i+1}" for i in range(len(D))]

    os.makedirs("results", exist_ok=True)
    D.to_csv("results/evaluation_matrix_step1.csv")
    print("[INFO] Preprocessing done → results/evaluation_matrix_step1.csv")

if __name__ == "__main__":
    preprocess()
import pandas as pd
w = pd.read_csv("results/bwm_weights.csv", index_col=0, header=None)
print(w)
print("Shape:", w.shape)