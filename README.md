

# 🧹 Data Sweeper: Cleaning & Visualization App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://data-sweeper-app-with-cleaning-and-visualization-4sgj4msgkjlti.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)

**Data Sweeper** is a powerful, web-based tool designed to streamline data processing tasks. Built with [Streamlit](https://streamlit.io/), this application allows users to upload raw datasets (CSV/Excel), perform automated cleaning operations, visualize key insights, and convert files into different formats instantly.

🔗 **Live Demo:** [Click here to use the app](https://data-sweeper-app-with-cleaning-and-visualization-4sgj4msgkjlti.streamlit.app/)

---

## 🚀 Features

### 1. Data Upload & Preview
*   Support for **CSV** and **Excel (.xlsx)** files.
*   View the first few rows of your dataset immediately after upload.
*   Display dataset dimensions (rows and columns).

### 2. Intelligent Data Cleaning
*   **Remove Duplicates:** Instantly identify and eliminate duplicate entries to ensure data integrity.
*   **Handle Missing Values:** Automatically fill missing numeric data with the **mean** of the column.
*   **Data Transformation:** Clean and standardize text data for consistency.

### 3. Interactive Visualization
*   **Bar Charts:** Visualize trends and comparisons across categories.
*   **Chart Configuration:** Select specific columns for X and Y axes to customize your view.

### 4. File Conversion & Export
*   **Format Conversion:** Seamlessly convert between **CSV** and **Excel** formats.
*   **Download Processed Data:** Export the cleaned and transformed dataset directly to your local machine.

---

## 🛠️ Tech Stack

*   **Frontend:** [Streamlit](https://streamlit.io/) (for the interactive web interface)
*   **Backend:** Python
*   **Data Processing:** [Pandas](https://pandas.pydata.org/)
*   **Visualization:** Matplotlib / Plotly (via Streamlit's native charts)
*   **File Handling:** OpenPyXL (for Excel support)

