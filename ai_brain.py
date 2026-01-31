import boto3
from langchain_aws import ChatBedrock

# 1. Setup the connection to the Brain
# (Make sure your computer is logged into AWS first!)
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1" # Use the region where you enabled Claude
)

# 2. Pick the model (Claude is like the smart professor)
llm = ChatBedrock(
    model_id="anthropic.claude-3-haiku-20240307-v1:0", # Use Haiku instead of Sonnet
    client=bedrock_client
)

# 3. Test the Brain
print("Asking the AI Brain a question...")
response = llm.invoke("Who is the blue dragon?")

print("\nAI Answer:")
print(response.content)