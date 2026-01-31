from elasticsearch import Elasticsearch
from langchain_aws import ChatBedrock

# 1. Connect to Library
es = Elasticsearch(cloud_id="db55515d970544adb8eefe322d037e67:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbTo0NDMkYzk3MTg3NzE1YzI0NGUzNThlZWNlYmU4MGMzNjk5MmEkMzY2ZWIwM2VlNTg5NDM0MjhkNjhlMTljYWExNTJiMWE=", api_key="cDA0UjZac0JNaTc5bWY0OE1YcXE6Zkdtc0N1bXJlb3VQWnJ4Ul9ScHc3dw==")

# 2. Connect to Brain (Using Haiku to avoid speed limits)
llm = ChatBedrock(model_id="anthropic.claude-3-haiku-20240307-v1:0")

# 3. The Robot's Mission
question = "Who is the blue dragon?"

# Step A: Search the library
search_results = es.search(index="my_stories", query={"match": {"content": question}})
context = search_results['hits']['hits'][0]['_source']['content']

# Step B: Tell the Brain the answer is in the context
prompt = f"Use this information: {context}. Question: {question}"

# Step C: Get the answer
response = llm.invoke(prompt)
print(response.content)