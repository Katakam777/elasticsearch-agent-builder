from elasticsearch import Elasticsearch

es = Elasticsearch(cloud_id="db55515d970544adb8eefe322d037e67:dXMtZWFzdC0yLmF3cy5lbGFzdGljLWNsb3VkLmNvbTo0NDMkYzk3MTg3NzE1YzI0NGUzNThlZWNlYmU4MGMzNjk5MmEkMzY2ZWIwM2VlNTg5NDM0MjhkNjhlMTljYWExNTJiMWE=", api_key="cDA0UjZac0JNaTc5bWY0OE1YcXE6Zkdtc0N1bXJlb3VQWnJ4Ul9ScHc3dw==")

# Let's add 3 new 'books' about the dragon
new_facts = [
    {
        "title": "Dragon Name",
        "content": "The blue dragon's name is Byte. He is a famous software engineer.",
        "author": "Library"
    },
    {
        "title": "Dragon Home",
        "content": "Byte the dragon lives in a cave located in Silicon Valley, Texas.",
        "author": "Library"
    },
    {
        "title": "Dragon Hobby",
        "content": "Besides Python, Byte loves to participate in Elasticsearch hackathons.",
        "author": "Library"
    }
]

for fact in new_facts:
    es.index(index="my_stories", document=fact)

print("Library updated! Byte now has a name and a home.")