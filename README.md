# 📄 AI_Contract_Analysis using Large Language Models (LLMs)

An end-to-end document processing pipeline that analyzes legal contracts from the **CUAD (Contract Understanding Atticus Dataset)** using Large Language Models (LLMs). The system extracts important legal clauses, generates concise contract summaries, and exports the results into CSV and JSON formats.

---

## 🚀 Features

- Load and preprocess CUAD legal contracts
- Normalize contract text
- Extract key legal clauses using LLMs
  - Termination Clause
  - Confidentiality Clause
  - Liability Clause
- Generate 100–150 word contract summaries
- Export results to CSV and JSON
- Modular Python architecture
- Environment variable support
- Bonus: Semantic Search using FAISS and Sentence Transformers

---

## 📂 Project Structure

```
AI_Contract_Analysis/
│
├── data/
│   └── CUADv1.json
│
├── output/
│   ├── contracts.csv
│   └── contracts.json
│
├── prompts/
│
├── config.py
├── data_loader.py
├── preprocessing.py
├── llm_pipeline.py
├── semantic_search.py
├── utils.py
├── main.py
│
├── requirements.txt
├── .env.example
├── README.md
│
└── notebooks/
```

---

## 🛠️ Tech Stack

- Python 3.10+
- Google Gemini API
- LangChain
- Pandas
- FAISS
- Sentence Transformers
- Python-dotenv

---

## 📊 Dataset

This project uses the **CUAD (Contract Understanding Atticus Dataset)**.

Dataset:
https://www.atticusprojectai.org/cuad

The assignment processes a subset of **50 legal contracts** for clause extraction and summarization.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI_Contract_Analysis.git

cd AI_Contract_Analysis
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 📁 Add Dataset

Place

```
CUADv1.json
```

inside

```
data/
```

---

## ▶️ Run Project

```bash
python main.py --input data/CUADv1.json --limit 50
```

---

## 📤 Output

After execution the project generates

```
output/

contracts.csv

contracts.json
```

Example CSV

| contract_id | summary | termination_clause | confidentiality_clause | liability_clause |
|-------------|----------|--------------------|-------------------------|------------------|
| Contract_001 | ... | ... | ... | ... |

---

## 🔄 Project Workflow

```
CUAD Dataset
      │
      ▼
Load Contracts
      │
      ▼
Preprocessing
      │
      ▼
LLM Analysis
      │
      ├─────────────► Clause Extraction
      │
      └─────────────► Contract Summary
                    │
                    ▼
             Export CSV / JSON
```

---

