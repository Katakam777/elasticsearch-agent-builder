from elasticsearch import Elasticsearch

client = Elasticsearch(cloud_id="db55515d970544adb8eefe322d037e67:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbTo0NDMkYzk3MTg3NzE1YzI0NGUzNThlZWNlYmU4MGMzNjk5MmEkMzY2ZWIwM2VlNTg5NDM0MjhkNjhlMTljYWExNTJiMWE=", api_key="cDA0UjZac0JNaTc5bWY0OE1YcXE6Zkdtc0N1bXJlb3VQWnJ4Ul9ScHc3dw==")

# Ask the library for anything about "dragons"
response = client.search(index="my_stories", query={"match": {"content": "dragon"}})

print("Found these stories:")
for hit in response['hits']['hits']:
    print(f"- {hit['_source']['title']} by {hit['_source']['author']}")