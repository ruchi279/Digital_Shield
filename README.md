# 🛡️ Digital Public Safety Shield

An AI-powered intelligence platform designed to detect, disrupt, and respond to "Digital Arrest" fraud networks and AI-voice spoofing scams in real-time. Built for **Problem Statement 6: AI for Digital Public Safety**.

## 🌐 Live Demo
* **Web Interface:** [Click here to test the live app]([YOUR_STREAMLIT_URL_HERE])
* **Backend API Documentation:** [Click here to view the live API](https://digital-shield-api.onrender.com/docs)

---

## 🚀 The Solution
In recent years, "Digital Arrest" scams have defrauded citizens of thousands by trapping victims in psychological hostage situations using spoofed numbers and AI-generated voices. 

This platform shifts public safety from reactive complaint tracking to proactive contact interception. It features a scalable, containerized API that analyzes communication streams across two dimensions:

1. **Behavioral Script Analysis:** State-machine logic that detects sequential psychological manipulation phases (Authority → Intimidation → Isolation → Financial Demand).
2. **Audio Intelligence:** Acoustic feature extraction (Spectral Centroids, Zero-Crossing Rates) to identify artificial variance profiles common in AI-cloned or VoIP-spoofed voices.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Docker
* **Frontend Prototype:** Streamlit
* **Audio Processing:** Librosa, NumPy

## ⚙️ How to Run Locally

### Prerequisites
* Docker installed and running on your machine.
* Python 3.10+ installed.

### Step 1: Run the API Backend (Docker)
Build the container and start the local server:
```bash
docker build -t digital_shield .
docker run -p 8000:8000 digital_shield
