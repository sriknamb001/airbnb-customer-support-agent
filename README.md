# 🤖 Airbnb Co-Host AI (Telegram Agent)

## Description:
Built an intelligent AI agent that acts as a 24/7 co-host for Airbnb guests via Telegram. The agent handles common guest questions using real-time conversation, memory, and custom tools — reducing the burden on hosts and improving guest experience.

## Highlights:

🧠 Multi-turn AI Agent: Remembers prior messages and maintains context across questions (e.g., “What time is check-in?” → “Can I arrive earlier?”).
🛠 Tool-Using Design: Agent uses custom functions to answer dynamic queries like check-in times, Wi-Fi passwords, and local recommendations.
💬 Telegram Bot Interface: Live, free, and public — accessible via a shareable Telegram bot link for easy demo and user interaction.
⚡ Fast + Affordable LLMs: Uses Claude 3 Haiku via OpenRouter (free tier) or open models via Hugging Face for intelligent, cost-free responses.
🔌 Modular Backend: Built with FastAPI and plug-and-play support for additional tools like availability lookups or personalized responses per listing.
Example Use Cases:

“Can I check in early?”
“Do you have Wi-Fi?”
“What’s a good coffee shop nearby?”
“Where can I park?”
Stack:

Telegram Bot API
FastAPI (Python)
Claude 3 Haiku via OpenRouter / Hugging Face
Custom tool functions (Python-based)
Optional: Supabase for persistence, Vercel / Fly.io for hosting
