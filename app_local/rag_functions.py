from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from openai import OpenAI

es_client = Elasticsearch('http://localhost:9200') 
model = SentenceTransformer("all-mpnet-base-v2")
client = OpenAI()

def elastic_search(query_string):
    index_name = "course-questions"

    search_term = query_string

    vector_search_term = model.encode(search_term)
    
    query = {
        "field": "text_vector",
        "query_vector": vector_search_term,
        "k": 5,
        "num_candidates": 10000, 
    }

    response = es_client.search(index=index_name, knn=query,source = ['Artículo','Título'])
    
    results_docs = []

    for hit in response['hits']['hits']:
        results_docs.append(hit['_source'])

    return results_docs

def build_prompt(query, search_results):
    prompt_template = """
You're an assistant that knows the mexican traffic regulations, more specific the Ciudad de México traffic regulations. 
Answer the QUESTION based on the CONTEXT from the database, also the answer is need it to be in spanish.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = ""
    
    for doc in search_results:
         context = context + f"Título: {doc['Título']}\nArtículo: {doc['Artículo']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

def rag(query):
    search_results = elastic_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer