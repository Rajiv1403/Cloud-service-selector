🌥️ Cloud Service Selection App (BWM + Markov + EWMA)

A Multi-Criteria Decision Making (MCDM) Model for Selecting the Best Cloud Service Provider

📌 Overview

Cloud providers (AWS, Azure, GCP, IBM, Oracle) offer different performance and cost benefits.
Companies struggle to pick the best provider based on their requirements.

This project solves that problem by combining:

BWM (Best Worst Method) – to compute criteria weights

Markov Chain Model – to calculate long-term performance

EWMA (Exponential Weighted Moving Average) – to smooth variations

Final Ranking Model – to give the best provider

It provides a Streamlit Web App + Docker Deployment.

🎯 Problem Statement

Selecting the best cloud service provider involves analyzing multiple QoS attributes:

Cost

Availability

Latency

Security

Flexibility

Scalability

Manual comparison is complex and inconsistent.
This app automates the process using MCDM techniques.

🚀 Features

✔ Preprocess dataset
✔ Compute BWM weights
✔ Build Markov Transition Matrix
✔ Apply EWMA smoothing
✔ Generate final ranking
✔ Easy-to-use web interface
✔ Fully Dockerized
✔ Supports custom datasets

🧠 Methodology
1️⃣ Data Preprocessing

Loads raw QoS dataset

Normalizes values

Creates evaluation matrix

2️⃣ Best Worst Method (BWM)

Identify Best & Worst criteria

Calculate pairwise importance

Compute optimized weights

3️⃣ Markov Model

Build state transition matrix

Predict long-term QoS behavior

4️⃣ EWMA Smoothing

Reduce noise

Stabilize Markov outputs

5️⃣ Final Ranking

Multiply BWM weights × Markov probabilities

Sort cloud providers

Produce final results

🖥️ Tech Stack
Category	Tools
Frontend	Streamlit
Backend Logic	Python
Algorithms	BWM, Markov Chain, EWMA
Data Processing	Pandas, NumPy
Deployment	Docker
Version Control	Git + GitHub
