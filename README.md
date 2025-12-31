# 📊 Universal Data File Uploader & Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Status](https://img.shields.io/badge/Status-Active-success)

## 🚀 Overview
In the Data Science and AI pipeline, the first bottleneck is often simply viewing the data. Whether it's a legacy **XML** file, a modern **Parquet** dataset, or a local **SQLite** database, switching between different tools to inspect schemas and row counts is inefficient.

**Universal Data File Uploader** is a Streamlit-based web application that acts as a unified interface for data ingestion. It instantly parses 8+ common file formats, providing immediate Exploratory Data Analysis (EDA), schema visualization, and standardization.

## ✨ Key Features
*   **Multi-Format Support:** Seamlessly handles `.csv`, `.xlsx`, `.json`, `.parquet`, `.tsv`, `.txt`, `.xml`, and `.sql/.db` files.
*   **Intelligent Database Parsing:** Automatically connects to uploaded SQLite files, extracts table names, and allows users to query specific tables via UI.
*   **Instant EDA (Exploratory Data Analysis):**
    *   Generates shape statistics (Rows/Columns) and memory usage.
    *   Detects data types and null values per column.
    *   Calculates descriptive statistics for numeric data automatically.
*   **Standardization:** Exports any uploaded format into a clean, standardized **CSV** file.
*   **Robust Error Handling:** Gracefully manages parsing errors and encoding issues.

## 🛠️ Tech Stack
*   **Frontend/UI:** [Streamlit](https://streamlit.io/) - For rapid application development and interactive components.
*   **Data Processing:** [Pandas](https://pandas.pydata.org/) - For data manipulation, DataFrame generation, and statistical analysis.
*   **Database Management:** `sqlite3` - For handling relational database files in memory.
*   **Utilities:** `json`, `os`, `tempfile` - For file system management and parsing.


## 🧠 Technical Challenges Solved
*   **SQLite Integration:** Handling `.db` files in a web interface required managing temporary files securely (`tempfile`) to allow the `sqlite3` engine to connect, query metadata, and extract tables before cleaning up the environment.
*   **Dynamic Parsing:** Implementing a routing logic to select the correct parsing engine (e.g., `read_parquet` vs `read_xml`) based on file signatures.

---
🔗 **Live Demo:** [Click here to use the app](https://data-sweeper-app-with-cleaning-and-visualization-4sgj4msgkjlti.streamlit.app/)

**Developed by [vijay]**
*Connect with me on [LinkedIn](https://www.linkedin.com/in/vijayarjun58/) | [Twitter](https://x.com/Vijay_yeripalli)*


