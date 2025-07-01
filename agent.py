from langchain.agents import initialize_agent, Tool
from langchain.llms import HuggingFaceHub
from tools import get_wifi_password, get_check_in_time, get_local_recs
from rag import get_rag_tool
import os

def get_agent(property_id, structured_data):
    tools = [
        Tool(name="get_wifi_password", func=lambda q: get_wifi_password(structured_data), description="Get the Wi-Fi password."),
        Tool(name="get_check_in_time", func=lambda q: get_check_in_time(structured_data), description="Get the check-in time."),
        Tool(name="get_local_recs", func=lambda q: get_local_recs(structured_data), description="Get local recommendations."),
        get_rag_tool(property_id)
    ]

    llm = HuggingFaceHub(
        repo_id="HuggingFaceH4/zephyr-7b-beta",  # Or another supported model
        huggingfacehub_api_token=os.getenv("HUGGINGFACE_TOKEN"),
        model_kwargs={
            "temperature": 0.7,
            "max_new_tokens": 200,
            "do_sample": True,
        }
    )

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent="chat-conversational-react-description",
        verbose=True
    )
