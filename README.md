# 🐲 Byte the Dragon: AI Research Assistant

Built for the **Elasticsearch Agent Builder Hackathon 2026**.

## 📖 Overview
Byte the Dragon is a Context-Driven AI assistant that uses **Retrieval-Augmented Generation (RAG)** to provide grounded, factual answers. By connecting **Elasticsearch** as a long-term memory and **AWS Bedrock (Claude 3 Haiku)** as the reasoning engine, the agent ensures that responses are strictly based on indexed data, eliminating AI hallucinations.

## 🛠️ Tech Stack
- **Search Engine:** Elasticsearch Cloud
- **LLM:** Anthropic Claude 3 Haiku (via AWS Bedrock)
- **Frontend:** Streamlit
- **Language:** Python



## 🚀 Getting Started

### 1. Installation
Clone the repository and install the dependencies:
```bash
pip install streamlit elasticsearch boto3 python-dotenv langchain-aws