import streamlit as st
import pandas as pd
import numpy as np
import os

import src.preprocess as preprocess_mod
import src.compute_bwm as bwm_mod
import src.markov_model as markov_mod
import src.ewma_smoothing as ewma_mod
import src.ranking as ranking_mod


# ------------------ ADVANCED CSS ------------------ #
st.markdown("""
<style>

body {
    background-color: #0d1117;
}

.main {
    background-color: transparent;
}

.sidebar .sidebar-content {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(255,255,255,0.2);
}

h1, h2, h3, h4 {
    color: white;
}

.dashboard-title {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
    background: linear-gradient(90deg, #6e8efb, #a777e3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding: 10px;
}

.card {
    background: rgba(255,255,255,0.07);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 25px;
    border: 1px solid rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
}

.custom-button {
    background: linear-gradient(135deg, #6e8efb, #a777e3);
    padding: 12px 25px;
    border-radius: 12px;
    color: white !important;
    font-weight: 700;
    border: none;
    width: 100%;
    transition: 0.3s;
}

.custom-button:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #5a73d7, #8a5fd1);
}

</style>
""", unsafe_allow_html=True)


# ------------------ SIDEBAR NAVIGATION ------------------ #
st.sidebar.title("⚙️ Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "📊 Preprocess Data",
        "⚖️ Compute BWM",
        "🔁 Markov Matrix",
        "📉 EWMA Smoothing",
        "🏆 Final Ranking"
    ]
)

# ------------------ PAGES ------------------ #

# HOME / DASHBOARD
if page == "🏠 Dashboard":
    st.markdown("<h1 class='dashboard-title'>Cloud Service Selector</h1>", unsafe_allow_html=True)
    st.write("### 👋 Welcome! Yeh system aapko **best cloud service choose karne** me madad karta hai.")
    st.write(
        """
        #### Automated Multi-Criteria Decision Making  
        Using **BWM + Markov + EWMA**  
        - High accuracy  
        - Zero manual calculation  
        - Fully automated workflow  
        """
    )

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("### 🚀 Start your analysis from left side menu!")
    st.markdown("</div>", unsafe_allow_html=True)


# ------------------ PREPROCESS ------------------ #
if page == "📊 Preprocess Data":
    st.markdown("<h2 class='dashboard-title'>Preprocess Dataset</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if st.button("🔧 Run Preprocessing", use_container_width=True):
        try:
            preprocess_mod.preprocess()
            st.success("Preprocessing Done! --> results/evaluation_matrix_step1.csv")
            st.dataframe(pd.read_csv("results/evaluation_matrix_step1.csv"))
        except Exception as e:
            st.error(e)

    st.markdown("</div>", unsafe_allow_html=True)


# ------------------ BWM ------------------ #
if page == "⚖️ Compute BWM":
    st.markdown("<h2 class='dashboard-title'>Compute BWM Weights</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if st.button("📘 Calculate BWM Weights", use_container_width=True):
        try:
            bwm_mod.compute_bwm()
            st.success("BWM Done! --> results/bwm_weights.csv")
            st.image("results/Figure4_BWM_Weights.png")
        except Exception as e:
            st.error(e)

    st.markdown("</div>", unsafe_allow_html=True)


# ------------------ MARKOV ------------------ #
if page == "🔁 Markov Matrix":
    st.markdown("<h2 class='dashboard-title'>Build Markov Transition Matrix</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if st.button("🔄 Build Markov Matrix", use_container_width=True):
        try:
            markov_mod.build_markov()
            st.success("Markov Transition Matrix Ready!")
            st.image("results/Figure3_Transition_Matrix.png")
        except Exception as e:
            st.error(e)

    st.markdown("</div>", unsafe_allow_html=True)


# ------------------ EWMA ------------------ #
if page == "📉 EWMA Smoothing":
    st.markdown("<h2 class='dashboard-title'>EWMA Smoothing</h2>", unsafe_allow_html=True)

    alpha = st.slider("EWMA Alpha Value", 0.0, 1.0, 0.3)

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if st.button("📉 Apply EWMA", use_container_width=True):
        try:
            ewma_mod.apply_ewma(alpha)
            st.success("EWMA Done!")
            st.image("results/Figure6_Convergence.png")
        except Exception as e:
            st.error(e)

    st.markdown("</div>", unsafe_allow_html=True)


# ------------------ FINAL RANKING ------------------ #
if page == "🏆 Final Ranking":
    st.markdown("<h2 class='dashboard-title'>Final Service Ranking</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if st.button("🏆 Generate Final Ranking", use_container_width=True):
        try:
            ranking_mod.rank_services()
            st.success("Final Ranking Ready!")
            st.image("results/Figure5_Final_Ranking.png")
            st.dataframe(pd.read_csv("results/final_ranking.csv").head(10))
        except Exception as e:
            st.error(e)

    st.markdown("</div>", unsafe_allow_html=True)
