from fastapi import FastAPI, Request
from agent import get_agent
import os, json, requests
from rag import match_property_id, get_rag_tool

app = FastAPI()
chat_histories = {}
user_state = {}
user_property_map = {}

def load_property_data(pid):
    with open(f"./data/properties/{pid}.json") as f:
        return json.load(f)

def send_msg(chat_id, text):
    token = os.getenv("TELEGRAM_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.post("/")
async def telegram_webhook(request: Request):
    data = await request.json()
    chat_id = str(data.get("message", {}).get("chat", {}).get("id"))
    msg = data.get("message", {}).get("text")

    if not chat_id or not msg:
        return {"ok": True}

    if chat_id not in user_state:
        user_state[chat_id] = "awaiting_property"
        send_msg(chat_id, "Hi! Which property are you referring to? Please send me the address or property name.")
        return {"ok": True}

    if user_state[chat_id] == "awaiting_property":
        property_id = match_property_id(msg)
        if property_id:
            user_property_map[chat_id] = property_id
            user_state[chat_id] = "ready"
            send_msg(chat_id, f"Thanks! I've identified the property as '{property_id}'. How can I assist you?")
        else:
            send_msg(chat_id, "Sorry, I couldn't identify the property. Please try again or provide a more detailed address.")
        return {"ok": True}

    property_id = user_property_map.get(chat_id)
    if not property_id:
        user_state[chat_id] = "awaiting_property"
        send_msg(chat_id, "Let's start over. Which property are you referring to?")
        return {"ok": True}

    property_data = load_property_data(property_id)
    chat_histories.setdefault(chat_id, []).append({"role": "user", "content": msg})

    rag_tool = get_rag_tool(property_id)
    agent = get_agent(property_id, property_data, rag_tool=rag_tool)

    result = agent.run(msg)
    chat_histories[chat_id].append({"role": "assistant", "content": result})

    send_msg(chat_id, result)
    return {"ok": True}
