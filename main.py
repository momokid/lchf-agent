import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = os.environ.get("LANGFLOW_ID")
FLOW_ID = os.environ.get("FLOW_ID")
APPLICATION_TOKEN = os.environ.get("APP_TOKEN") #
ENDPOINT = "lcf_waterproject" # The endpoint name of the flow



def run_flow(message: str) -> dict:
   
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    
    st.set_page_config(
    page_title="Leading-Edge Charity Foundation - User Engagement",
    page_icon="🧊",
    )
    
    
    st.title("LCHF User Engagement Board")
    message = st.text_area("Message",placeholder="Ask about your project...")
    
    if st.button("Submit Question"):
        if not message.strip():
            st.error("For me to answer accurately, please provide the following; Soil Type, Rocky Terrain, Nearest River Distance, Underground Water Depth")
            return
        
        try:
            with st.spinner("A moment please..."):
                response = run_flow(message)
            
            response = response['outputs'][0]['outputs'][0]['results']['message']['text']
            st.markdown(response)
            
        except Exception as e:
            st.error(str(e))
            
if __name__ == "__main__":
    main()