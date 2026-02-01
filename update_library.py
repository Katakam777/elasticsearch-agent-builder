from elasticsearch import Elasticsearch

es = Elasticsearch(cloud_id="ELASTIC_CLOUD_ID", api_key="ELASTIC_API_KEY")

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