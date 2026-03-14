# 🚀 Automated Lead Integration Engine
### From Google Sheets to API with Zero Manual Effort

Yo! This is a project I built to solve a common headache: **manual data entry.** I’ve engineered a pipeline that takes leads from a Google Sheet, processes them, sends them to an external API (like Roofle or GoHighLevel) via HTTP POST, and then updates the database status in real-time. 

## 🛠 The Tech Stack
* **Python (Pandas):** For initial data cleaning and preparation.
* **Google Sheets API:** As the primary database.
* **Make.com (Integromat):** The "brain" of the automation.
* **REST API / JSON:** For transmitting data to third-party services.

## 🏗 System Architecture
It’s basically a three-stage circuit:
1.  **The Trigger:** A new row is detected in Google Sheets.
2.  **The Logic:** Make.com maps the data into a clean JSON payload.
3.  **The Feedback Loop:** Once the API receives the data, the system writes "Success" and a timestamp back to the original Sheet. No duplicates, no ghosting.

## 📁 What's Inside?
* `/scripts`: Python scripts used for data simulation.
* `/blueprint`: The Make.com `.json` blueprint (import this to see the magic).
* `/docs`: Screenshots of the successful data flow.

## ⚡ Key Features
* **Error Handling:** Built-in logic to handle failed requests.
* **Real-time Logging:** Every entry gets a timestamp and status update.
* **Scalable:** Works for 10 leads or 10,000 leads without breaking a sweat.

---
*Built with ☕ and logic by **Sandi**.*
*Electrical Engineer turned Automation Enthusiast.*
