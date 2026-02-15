# 🍽️ Zomato Bangalore — RAG-Powered Restaurant Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot built on the Zomato Bangalore Restaurants dataset that allows users to ask natural-language questions about restaurants, menus, ratings, locations, cuisines, and reviews.

Instead of hallucinating answers like a standard LLM, this system retrieves relevant restaurant data from a vector database and generates **context-aware, fact-grounded responses**.

---

## 🚀 Project Overview

This project demonstrates how to build a **production-style GenAI application** using structured CSV data.

The pipeline:

1. 📂 Load & preprocess Zomato Bangalore restaurant dataset
2. 🧠 Generate embeddings using a HuggingFace model
3. 🗂️ Store vectors in Chrome Vector Store
4. 🔎 Perform semantic retrieval
5. 🤖 Generate responses using Anthropic's Claude model
6. 🛡️ Apply prompt engineering for safe & accurate outputs
7. 📊 Evaluate retrieval precision & response relevance

---

## 🏗️ System Architecture

User Query
→ Embedding Generation
→ Vector Store Retrieval
→ Context Injection
→ LLM Response Generation
→ Final Answer

This ensures responses are grounded in real restaurant data.

---

## 🛠️ Tech Stack

* **LLM:** Anthropic Claude
* **Embeddings:** HuggingFace Transformers
* **Vector Store:** Chrome Vector Store
* **Language:** Python
* **Data Source:** Zomato Bangalore Restaurants CSV

---

## 💡 Example Queries

* “Best rated restaurants in Indiranagar?”
* “Affordable North Indian restaurants under ₹500?”
* “Romantic dining places in Bangalore with 4+ rating”
* “Restaurants with outdoor seating and live music”
* “Top brunch spots in Koramangala”

---

## 📂 Dataset

The chatbot is built on the **Zomato Bangalore Restaurants dataset**, which includes:

* Restaurant Name
* Location
* Cuisines
* Cost for two
* Ratings
* Reviews
* Online order availability
* Table booking availability

---

## 🧠 Why RAG?

Traditional LLMs:

* ❌ Hallucinate answers
* ❌ Cannot access updated datasets

RAG-based systems:

* ✅ Retrieve real facts
* ✅ Provide grounded responses
* ✅ Work with private/custom datasets
* ✅ Improve reliability

---

## 🛡️ Prompt Engineering

The system includes:

* Context injection templates
* Instructions to avoid hallucination
* Safe fallback responses when data is missing
* Controlled answer formatting

If relevant data is not found, the bot responds transparently instead of guessing.

---

## 📊 Evaluation Metrics

To iteratively improve performance, we track:

* 🔎 Retrieval Precision
* 🎯 Response Relevance
* 📚 Fact Consistency

This helps refine embedding quality and prompt design.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/zomato-rag-chatbot.git
cd zomato-rag-chatbot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Keys

Create a `.env` file:

```
ANTHROPIC_API_KEY=your_key_here
```

---

## ▶️ Running the Application

```bash
python main.py
```

---

## 📈 Future Improvements

* 🔥 Deploy on Streamlit / FastAPI
* 📊 Add feedback-based retraining loop
* 🧠 Hybrid search (keyword + semantic)
* 🌐 Multi-city support
* 📱 Web UI with chat history

---

## 🎯 Learning Outcomes

This project helps you understand:

* How RAG systems work internally
* Embedding generation & similarity search
* Vector database integration
* LLM prompt conditioning
* Building production-ready GenAI apps

---

## 📜 License

MIT License

---

## 🤝 Contributing

Pull requests are welcome!
If you’d like to improve retrieval quality, UI, or evaluation metrics — feel free to contribute.

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share with other GenAI learners

---

**Built with ❤️ for GenAI & LLM Engineers**
