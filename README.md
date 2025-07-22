**This Project is based off of Tech With Tim's Advanced AI Agent Video, Be Sure to check it out to understand how this works**

# 🤖 Research Assistant

**Research Assistant** is a local AI-powered agent that helps developers find alternatives to developer tools, frameworks, platforms, and APIs.

Just enter a query like:

```
"Alternatives to Firestore"
```

Research Assistant will:
1. Use **SerpAPI** to search the web.
2. Use **Crawl4AI** to extract markdown content from relevant URLs.
3. Run a structured, multi-step **LangGraph** workflow.
4. Output structured summaries with top alternatives and rationale.

---

## 🧠 Tech Stack

- **LangChain** + **LangGraph** — for modular, layered agent workflows
- **Crawl4AI** — headless browser-based web scraping with Markdown output
- **SerpAPI** — Google search API for developer-friendly search
- **Ollama + LLaMA2** — fast, local LLM inference (if configured)

---

## 🛠️ Setup Instructions

> ⚠️ Make sure you have Python 3.10+ and `pip` installed.

### 1. Clone the repository

```bash
git clone https://github.com/Winston-Dmello/Research-Agent.git
cd Research_Agent
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API keys in `.env`

Create a `.env` file in the root directory with the following contents:

```env
SERPAPI_API_KEY=your_serpapi_key
```

---

## 🚀 How to Run

Run the assistant with a query:

```bash
python main.py
```

You will be prompted:

```text
What tool are you researching? >> firestore alternatives
```

The assistant will:
- Search relevant web content
- Scrape key links
- Run LLM analysis
- Print structured results like:

```
Top Alternatives to Firestore:

1. Supabase - Open-source backend with realtime DB.
2. PlanetScale - Scalable MySQL with branch-based workflow.
3. AWS DynamoDB - Fully managed serverless NoSQL.
...
```

---

## 📂 Project Structure

```bash
Research_Assistant/
├── main.py              # Entry point for running the assistant
├── .env                 # API keys (ignored in Git)
├── requirements.txt     # Project dependencies
└── src/
    ├── crawl.py         # Handles Crawl4AI web scraping
    ├── models.py        # LangChain + LLM setup
    ├── prompts.py       # Prompt templates for the LLM
    ├── workflow.py      # LangGraph multi-step logic
```

---

## 🔐 .gitignore Recommendation

Make sure to exclude these from Git:

```gitignore
.env
env/
__pycache__/
*.pyc
```

---

## 🧪 Coming Soon

- [ ] GUI interface using Streamlit or Gradio
- [ ] Local embeddings + vector search
- [ ] PDF export of reports

---

## 🙌 Credits
- [TechWithTim](https://youtu.be/xekw62yQu14?si=Fi4BMXRMikdn8fqZ)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://python.langchain.com/)
- [SerpAPI](https://serpapi.com/)
- [Crawl4AI](https://github.com/KnowledgeGPT/crawl4ai)
