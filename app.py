
import os
from dotenv import load_dotenv
load_dotenv()

# Now use these variables instead of hardcoded strings
CLOUD_ID = os.getenv("ELASTIC_CLOUD_ID")
API_KEY = os.getenv("ELASTIC_API_KEY")



import streamlit as st  # <--- THIS IS THE MISSING LINE!
import boto3
from elasticsearch import Elasticsearch
from langchain_aws import ChatBedrock


with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f4/Elasticsearch_logo.svg", width=50)
    st.title("Project Info")
    st.markdown("**Hackathon:** Elasticsearch Agent Builder")
    st.markdown("**Developer:** Sandeep Katakam")
    st.markdown("**Brain:** Claude 3 Haiku via AWS Bedrock")
    st.markdown("**Library:** Elasticsearch Cloud")
    st.divider()
    st.write("This agent uses RAG (Retrieval-Augmented Generation) to answer questions based strictly on your private data.")




import streamlit as st
import boto3
from elasticsearch import Elasticsearch
from langchain_aws import ChatBedrock

# --- CONFIGURATION ---
st.set_page_config(page_title="Byte's AI Assistant", page_icon="🐲")
st.title("🐲 Byte's AI Assistant")

# Initialize Connections
CLOUD_ID = "ELASTIC_CLOUD_ID"
API_KEY = "ELASTIC_API_KEY"

es = Elasticsearch(cloud_id=CLOUD_ID, api_key=API_KEY)
bedrock_client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
llm = ChatBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0", client=bedrock_client)

# --- UI LOGIC ---
query = st.text_input("Ask Byte a question:", placeholder="e.g., Where does Byte live?")

if query:
    with st.spinner("Searching Byte's Library..."):
        # 1. Search Elasticsearch
        res = es.search(index="my_stories", query={"match": {"content": query}})
        
        if res['hits']['hits']:
            context = res['hits']['hits'][0]['_source']['content']
            
            # 2. Generate Answer
            prompt = f"Using this info: {context}. Answer this: {query}"
            response = llm.invoke(prompt)
            # 3. Create your STRICT prompt using the 'context' we just made
            strict_prompt = f"""
            INSTRUCTIONS:
            1. Answer the Question using ONLY the provided Information.
            2. If the answer is not directly stated in the Information, respond with exactly: "I do not have that information in my library."
            3. Do NOT provide explanations or outside knowledge.

            Information: {context}
            Question: {query}
            """
            
            # 4. Send it to the AI Brain
            response = llm.invoke(strict_prompt)
            
            st.subheader("Robot Answer:")
            st.write(response.content)
            
            with st.expander("See the Library Source"):
                st.info(f"Source Text: {context}")
        else:
            st.warning("I couldn't find that in the library!")


