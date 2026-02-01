from elasticsearch import Elasticsearch

client = Elasticsearch(cloud_id="ELASTIC_CLOUD_ID", api_key="ELASTIC_API_KEY")

# Ask the library for anything about "dragons"
response = client.search(index="my_stories", query={"match": {"content": "dragon"}})

print("Found these stories:")
for hit in response['hits']['hits']:
    print(f"- {hit['_source']['title']} by {hit['_source']['author']}")