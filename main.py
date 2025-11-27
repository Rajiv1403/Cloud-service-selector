# main.py — full pipeline
import os, glob

# Clean old images
os.makedirs("results", exist_ok=True)
for f in glob.glob("results/*.png"):
    os.remove(f)
print("[INFO] Cleaned old result files.\n")

# Import all modules
from preprocess import preprocess
from compute_bwm import compute_bwm
from markov_model import build_markov
from ewma_smoothing import apply_ewma
from ranking import rank_services

if __name__ == "__main__":
    print("========== STARTING PIPELINE ==========\n")

    print("[1/5] Preprocessing dataset...")
    preprocess()

    print("\n[2/5] Computing BWM weights...")
    compute_bwm()

    print("\n[3/5] Building Markov transition matrix...")
    build_markov()

    print("\n[4/5] Applying EWMA smoothing...")
    apply_ewma(alpha=0.3)

    print("\n[5/5] Calculating final ranking...")
    rank_services()

    print("\n✅ Pipeline completed! All outputs saved in 'results/' folder.")
