
# MultiAgent Industry Explorer and Opportunity Finder

This project implements a Multi-Agent system that conducts market research, analyzes AI/ML/GenAI trends, generates use cases, and collects relevant datasets for any given Company or Industry. 

---

## 📋 Project Overview 

- **Research Agent**: Gathers company/industry details via Serper API and scraping.
- **Use Case Generation Agent**: Creates 5 GenAI/AI/ML use cases based on industry trends (referencing McKinsey, Deloitte, Nexocode insights).
- **Resource Asset Agent**: Finds relevant datasets from Kaggle and HuggingFace.
- **Proposal Generator**: Compiles results into a structured, downloadable Markdown file.
- **Streamlit Web App**: Provides an intuitive UI for proposal generation and download.

---

##  System Architecture

```text
[User Input]
      ↓
[Research Agent]
      ↓
[Use Case Generation Agent]
      ↓
[Resource Asset Collection Agent]
      ↓
[Proposal Generator]
      ↓
[Streamlit App]
```

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai_usecase_generator
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # (Mac/Linux)
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**:
   Add your API keys:
   ```dotenv
   GROQ_API_KEY=your-groq-api-key
   SERPER_API_KEY=your-serper-api-key
   KAGGLE_USERNAME=your-kaggle-username
   KAGGLE_KEY=your-kaggle-api-key
   ```

5. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

---

## 📂 Project Structure

```text
├── agents/
│   ├── research.py
│   ├── usecase.py
│   ├── resources.py
├── utils/
│   ├── search.py
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── proposal.md (Generated after running)
├── .gitignore
├── .env (local only, not pushed)
```

---

## 📄 Deliverables

- Source Code
- Streamlit Application
- Final Proposal (Markdown)
- Architecture Flowchart
- Final Project Report
- Demo Video (showcasing app + flowchart)

---

## 📊 Technologies Used

- Python 3.12
- LangChain
- Groq API (Llama 3)
- Serper API
- Kaggle API
- HuggingFace Datasets
- Streamlit
- dotenv
- BeautifulSoup

---

## 🎯 Objective

To automate AI opportunity discovery by:
- Conducting deep market research
- Generating practical AI/GenAI/ML use cases
- Providing starter datasets for quick implementation

---

## 🙌 Acknowledgements

- McKinsey & Company
- Deloitte Insights
- Nexocode AI Reports
- HuggingFace Datasets
- Kaggle Open Datasets

---
