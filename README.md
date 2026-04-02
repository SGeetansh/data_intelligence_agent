# 🚀 Data Intelligence Agent

NOTE: THIS README IS A WORK IN PROGRESS

A modular multi-agent system for data analytics and machine learning, built using Google's Agent Development Kit (ADK), BigQuery, and LLM-powered reasoning.

---

## 🧠 Overview

This project implements a **multi-agent architecture** that can:

* Convert natural language → SQL queries (NL2SQL)
* Execute queries on BigQuery
* Perform data analysis using Python (NL2Py)
* Train and evaluate models using BigQuery ML (BQML)
* Generate insights and summaries using LLMs

The system is designed to move beyond simple queries into **end-to-end data intelligence workflows**.

---

## 🏗️ Architecture

The system follows a **hierarchical agent design**:

* **Top-Level Agent**

  * Routes user queries to appropriate sub-agents

* **Database Agent (NL2SQL)**

  * Converts natural language into SQL
  * Validates and executes queries on BigQuery

* **Data Science Agent (NL2Py)**

  * Generates Python code for analysis and visualization
  * Executes code and returns results

* **BQML Agent**

  * Handles model training and evaluation within BigQuery

---

## 📁 Project Structure

```
data_intelligence_agent/
├── subagents/
│   ├── bigquery/
│   │   ├── agent.py
│   │   ├── prompts.py
│   │   └── tools.py
│   │
│   ├── analytics/
│   └── bqml/
│
├── utils/
│   └── utils.py
│
├── agent.py
├── instructions.py
├── tools.py
├── pyproject.toml
└── README.md
```

---

## ⚙️ Setup

### 1. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add to PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

### 2. Install Dependencies

```bash
poetry install
```

---

### 3. Activate Environment

```bash
poetry shell
```

---

### 4. Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
BQ_PROJECT_ID=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
```

---

## ▶️ Running the Agent

```bash
poetry run python agent.py
```

---

## 🛠️ Key Features

* 🔄 Multi-agent orchestration
* 🧾 NL → SQL generation with validation
* 📊 Python-based data analysis
* 🤖 LLM-driven reasoning and summarization
* ☁️ Native BigQuery + BQML integration

---

## 🧪 Example Queries

* "Show top 10 customers by revenue"
* "What caused the drop in sales last month?"
* "Train a churn prediction model"
* "Plot revenue trends over time"

---

## 🧩 Tech Stack

* Python (Poetry)
* Google ADK
* BigQuery
* Gemini (LLM)
* Pandas / Matplotlib

---

## 🚧 Future Improvements

* Add memory and context tracking
* Improve query routing logic
* Add caching for repeated queries
* Build UI (Streamlit / React)
* Deploy as API (FastAPI)

---

## 📌 Why This Project?

This project demonstrates:

* Multi-agent system design
* LLM orchestration
* Real-world data engineering + ML workflows
* Production-oriented architecture

---

## 👤 Author

**Geetansh Saxena**

---

## ⭐ Contributing

Pull requests and ideas are welcome!
