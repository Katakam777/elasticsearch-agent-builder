from elasticsearch import Elasticsearch

# 1. Put your secret codes here!
CLOUD_ID = "db55515d970544adb8eefe322d037e67:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbTo0NDMkYzk3MTg3NzE1YzI0NGUzNThlZWNlYmU4MGMzNjk5MmEkMzY2ZWIwM2VlNTg5NDM0MjhkNjhlMTljYWExNTJiMWE="
API_KEY = "cDA0UjZac0JNaTc5bWY0OE1YcXE6Zkdtc0N1bXJlb3VQWnJ4Ul9ScHc3dw=="

# 2. Connect to the Library
client = Elasticsearch(
    cloud_id=CLOUD_ID,
    api_key=API_KEY
)

# 3. Check if it works (The Handshake)
print("Checking connection...")
print(client.info())

# 4. Create a "Shelf" (Index) and add a "Book" (Document)
first_book = {
    "title": "The Blue Dragon",
    "content": "Once upon a time, there was a blue dragon who loved to code in Python.",
    "author": "Gemini"
}

# This sends the book to the library
response = client.index(index="my_stories", document=first_book)

print(f"Success! Book added. ID is: {response['_id']}")