# 🔍 Data.gov Search Platform
> A Google-style dataset search and exploration tool built with Python and Streamlit

---

## 📋 Project Overview

This project is a **Streamlit web application** that allows users to search, browse, and explore public datasets from [data.gov](https://data.gov). It replicates a Google-style search experience — users type a keyword, browse matching datasets, and instantly explore the data without downloading anything manually.

| Field | Details |
|-------|---------|
| **Built With** | Python, Streamlit, Pandas, Requests |
| **Data Source** | data.gov (U.S. Government Open Data) |
| **App Type** | Interactive Web Application |
| **Data Formats Supported** | CSV, TSV, XLS, XLSX |

---

## ✨ Features

- **🔎 Keyword Search** — Search datasets by name or description keyword
- **📋 Dataset Dropdown** — Select from matching datasets via dynamic dropdown menu
- **📄 Resource Display** — View resource name, format, and download URL for each dataset
- **📊 Data Exploration** — Click to explore any resource:
  - Top 10 records preview
  - Total number of records
  - Number of columns
  - Data types of each column
  - Basic statistics (min, max, mean, std)
- **🌐 Live HTTP Requests** — Data is fetched in real time from data.gov using the resource download URL

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core application language |
| **Streamlit** | Web interface framework |
| **Pandas** | Data loading, filtering, and profiling |
| **Requests** | HTTP requests to fetch live dataset resources |
| **data.gov API** | Source of dataset metadata and resources |

---

## 🚀 How to Run the App

### Prerequisites
Make sure you have Python installed, then install the required libraries:

```bash
pip install -r requirements.txt
```

### Run the App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
Data-Gov-Search-Platform/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── datasets_metadata1.csv    # Dataset metadata from data.gov
├── datasets_resources1.csv   # Dataset resources from data.gov
└── README.md                 # Project documentation
```

---

## 💡 How It Works

```
[1] App loads dataset metadata and resources from local CSV files
        └─► datasets_metadata1.csv — dataset names, IDs, descriptions
        └─► datasets_resources1.csv — resource URLs, formats, names

[2] User types a search keyword
        └─► App filters datasets by name OR description match
        └─► Case-insensitive search using pandas string matching

[3] Matching datasets displayed in dropdown menu
        └─► User selects a dataset to explore

[4] Resources for selected dataset are displayed
        └─► Resource name, format, and download URL shown

[5] User clicks "Explore" on a resource
        └─► App sends HTTP GET request to the resource download URL
        └─► Data loaded into pandas DataFrame based on format (CSV/TSV/Excel)
        └─► Top 10 records, statistics, and data profile displayed
```

---

## 📸 App Preview

### Search Interface
- User enters keyword (e.g., "climate", "housing", "health")
- Matching datasets appear in a dropdown

### Dataset Exploration
- Top 10 records shown in an interactive table
- Record count, column count, data types, and statistics displayed

---

## 🎯 What I Learned

- Building interactive web applications with **Streamlit**
- Working with **REST APIs** and live HTTP requests in Python
- Data profiling and exploration using **Pandas**
- Handling multiple data formats (CSV, TSV, Excel) dynamically
- Filtering and searching large datasets efficiently
- Working with real-world **open government data** from data.gov

---

## 👨‍💻 Author

**Zufan Wabe**
Data Analyst | Junior Security Analyst | CYDEO Cybersecurity Bootcamp
CompTIA Security+ Certified
[LinkedIn](https://www.linkedin.com/in/zufan-wabe-3bb171294)

---

*Built as part of a Data Analytics project using publicly available U.S. government data from data.gov*
