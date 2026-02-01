import streamlit as st
import os
import boto3
from elasticsearch import Elasticsearch
from langchain_aws import ChatBedrock

# 1. MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Byte's AI Assistant", page_icon="🐲")

# 2. LOAD SECRETS CORRECTLY
# This looks for the values in your Streamlit "Secrets" dashboard
CLOUD_ID = st.secrets.get("ELASTIC_CLOUD_ID")
API_KEY = st.secrets.get("ELASTIC_API_KEY")
AWS_ID = st.secrets.get("AWS_ACCESS_KEY_ID")
AWS_SECRET = st.secrets.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = st.secrets.get("AWS_DEFAULT_REGION", "us-east-1")

# 3. STOP IF KEYS ARE MISSING
if not CLOUD_ID or not API_KEY:
    st.error("❌ Missing Elasticsearch Credentials in Streamlit Secrets!")
    st.stop()

# 4. INITIALIZE CONNECTIONS
@st.cache_resource # Keeps connection alive so it doesn't reconnect every click
def init_connections():
    es = Elasticsearch(cloud_id=CLOUD_ID, api_key=API_KEY)
    bedrock_client = boto3.client(
        service_name="bedrock-runtime", 
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ID,
        aws_secret_access_key=AWS_SECRET
    )
    llm = ChatBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0", client=bedrock_client)
    return es, llm

es, llm = init_connections()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f4/Elasticsearch_logo.svg", width=50)
    st.title("Project Info")
    st.markdown("**Hackathon:** Elasticsearch Agent Builder")
    st.markdown("**Developer:** Sandeep Katakam")
    st.markdown("**Brain:** Claude 3 Haiku (AWS Bedrock)")
    st.divider()
    st.write("This agent uses RAG to answer questions based strictly on your private data.")

# --- UI LOGIC ---
st.title("🐲 Byte's AI Assistant")
query = st.text_input("Ask Byte a question:", placeholder="e.g., Where does Byte live?")

if query:
    with st.spinner("Searching Byte's Library..."):
        # 1. Search Elasticsearch
        res = es.search(index="my_stories", query={"match": {"content": query}})
        
        if res['hits']['hits']:
            context = res['hits']['hits'][0]['_source']['content']
            
            # 2. Create the STRICT prompt
            strict_prompt = f"""
            INSTRUCTIONS:
            1. Answer the Question using ONLY the provided Information.
            2. If the answer is not in the Information, say: "I do not have that info."
            
            Information: {context}
            Question: {query}
            """
            
            # 3. Generate Answer
            response = llm.invoke(strict_prompt)
            
            st.subheader("Robot Answer:")
            st.write(response.content)
            
            with st.expander("See the Library Source"):
                st.info(f"Source Text: {context}")
        else:
            st.warning("I couldn't find that in the library!")