# 🚀 Automated Lead Integration Engine
**Zero-Manual-Effort Pipeline: Google Sheets ↔️ Third-Party APIs**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Make.com](https://img.shields.io/badge/Orchestrator-Make.com-purple.svg?style=for-the-badge&logo=make)
![Google Sheets](https://img.shields.io/badge/Database-Google_Sheets-green.svg?style=for-the-badge&logo=googlesheets)
![API](https://img.shields.io/badge/Integration-REST_API-red.svg?style=for-the-badge)

---

## 📌 Project Overview
Stop wasting hours on manual data entry. I engineered this **Automated Lead Integration Engine** to bridge the gap between static lead lists and active CRM systems. It functions as a "Digital Circuit," detecting new entries in real-time and synchronizing them across high-ticket platforms like **GoHighLevel**, **Roofle**, or any custom REST API.

---

## 🏗️ System Architecture: The Three-Stage Circuit

The engine operates on a seamless feedback loop:

### 1️⃣ The Trigger (Input) 📍
A new lead is added to the Google Sheets "Database." The system monitors for changes using a high-frequency polling webhook.

### 2️⃣ The Logic (Middleware) 🧠
Using **Make.com (Integromat)** as the brain, the system:
* Cleans and maps the data using **Python (Pandas)** logic.
* Constructs a precise **JSON Payload**.
* Handles multi-step transformations (Name splitting, Phone formatting).

### 3️⃣ The Feedback Loop (Output) 🔄
* **POST Request:** Data is transmitted to the destination API.
* **Success Logging:** Once the API responds (200 OK), the system writes a "Success" tag and a **Live Timestamp** back to the Google Sheet.
* **Error Shield:** If the API fails, it logs the error code for immediate troubleshooting—**No more ghosted leads.**

---

## 🛠️ Tech Stack & Components

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Data Cleaning** | Python (Pandas) | Initial data simulation & validation |
| **Cloud Logic** | Make.com (Integromat) | Workflow orchestration & API mapping |
| **Source DB** | Google Sheets API | Primary data entry & status logging |
| **Transmission** | REST API / JSON | Secure data sync to CRMs (GoHighLevel/Roofle) |

---

## ⚡ Key Features

* **🛡️ Duplication Protection:** Built-in filters to ensure one lead only gets synced once.
* **📈 Massive Scalability:** Engineered to handle 10 or 10,000 leads without a single drop in performance.
* **⏱️ Real-time Tracking:** Every sync is timestamped, creating a perfect audit trail for sales teams.
* **🚦 Error Handling:** Automatic "Fail-Safe" logic to notify the user if a request breaks.

---

## 📂 Project Structure

```text
├── scripts/
│   └── data_sim.py         # Python logic for cleaning raw inputs
├── blueprint/
│   └── scenario.json       # Make.com Blueprint (Import this to your dashboard)
├── docs/
│   └── workflow_demo.png   # Visualization of the data flow
└── README.md
