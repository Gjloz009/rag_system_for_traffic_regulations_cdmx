from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
import json
from tqdm.auto import tqdm

model = SentenceTransformer("all-mpnet-base-v2")
es_client = Elasticsearch('http://elasticsearch:9200')

with open('documents-with-ids.json', 'rt') as f_in:
    docs_withids_raw = json.load(f_in)
    
docs_without_table = [{key1: d[key1], key2: d[key2], key3: d[key3]} for d in docs_withids_raw for key1, key2, key3 in [("Título", "Artículo","id")]]

#created the dense vector using the pre-trained model
operations = []
print("Encoding ...")
for doc in tqdm(docs_without_table):
    # Transforming the title into an embedding using the model
    doc["text_vector"] = model.encode(doc["Artículo"]).tolist()
    operations.append(doc)

index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "Título": {"type": "text"},
            "Artículo": {"type": "keyword"},
            "id": {"type": "keyword"},
            "text_vector": {"type": "dense_vector", "dims": 768, "index": True, "similarity": "cosine"},
        }
    }
}


index_name = "articulos-index"

es_client.indices.delete(index=index_name, ignore_unavailable=True)
es_client.indices.create(index=index_name, body=index_settings)

print("indexing elastic ...")
for doc in tqdm(operations):
    try:
        es_client.index(index=index_name, document=doc)
    except Exception as e:
        print(e)