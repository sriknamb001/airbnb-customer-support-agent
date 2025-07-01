# 🏡 Airbnb Concierge Bot

**AI-powered Telegram bot** that acts as a smart Airbnb concierge. It answers guest questions using a memory-aware, tool-using agent powered by OpenAI and LangChain, with Retrieval-Augmented Generation (RAG) over custom property data.

---

## 🧠 How It Works

1. **Telegram Bot Frontend**  
   Guests interact with the bot directly via Telegram.

2. **Agentic AI Backend**  
   Powered by **LangChain + LangGraph**, the bot uses an LLM-driven agent with tool capabilities:

   - 🔍 **RAG** via ChromaDB for fetching relevant context from property-specific documents
   - 🛠️ Tool-calling for handling structured data lookups

3. **Scoped Knowledge per Property**  
   Each Airbnb listing has its own JSON file with property-specific details (check-in, Wi-Fi, parking, etc).

4. **FastAPI Server**  
   Handles webhook communication and request routing.

---

## 💡 Features

- ✅ Answers detailed guest questions using RAG + memory
- ✅ Multi-turn, context-aware conversations
- ✅ Handles multiple listings with scoped knowledge
- ✅ Pluggable JSON data for quick property updates
- ✅ Works via any Telegram account

---

## 🔧 Tech Stack

| Tech             | Purpose                         |
| ---------------- | ------------------------------- |
| FastAPI          | Backend server                  |
| Telegram Bot API | Guest messaging interface       |
| LangChain        | Agent + tool orchestration      |
| LangGraph        | Multi-turn agent state handling |
| ChromaDB         | Vector database for RAG         |
| OpenAI API       | LLM completions                 |
| dotenv           | Environment variable management |

---

## 📂 Project Structure
