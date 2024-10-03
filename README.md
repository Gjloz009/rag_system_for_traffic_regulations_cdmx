# RAG system for CDMX Traffic Regulations
### version 0.1.2
---

<p align="center">
  <img src="images\650_1200.jpg">
</p>

---
Patches for 0.1.2 version:
- implemented hybrid search.
---
## Index
- 1.[Objective and description of the problem](#1-objective-and-description-of-the-problem)
- 2.[Technologies](#2-technologies)
  - 2.1.[Host machine technologies](#21-host-machine-technologies)
- 3.[Data Architecture](#3-data-architecture)
- 4.[Instructions on how to replicate the project](#4-instructions-on-how-to-replicate-the-project)
- 5.[Future enhancements](#5-future-enhancements)

---
## 1. Objective and description of the problem
<p align="justify">
Traffic regulations documents play a crucial role in the development of cities around the world. This project aims to create a RAG (Retrieval-Augmented Generation) system for the traffic regulation document of Mexico City, Mexico. The target population for the project includes new drivers who are unfamiliar with the various articles that exist, as well as experienced drivers who have questions or doubts about any article in the document. The goal is to help these drivers better understand and navigate the traffic regulations.
</p>

I'm attacching the link to the traffic regulations document, the document is in Spanish:
>https://www.ssc.cdmx.gob.mx/storage/app/media/Transito/Actualizaciones/Reglamento-de-Transito-CDMX.pdf

## 2. Technologies
For setting up the VM Instance or Local Machine please install these tools:
- Docker
- docker-compose
  
If you want steps for installing those tools, please check [`here`](./create_instance.md).

### 2.1  Host machine technologies
For this version it is all constructed in python using python libraries.
- <p align="justify">
  <b>Docker</b> : for creating the web-app image.
  </p>
- <p align="justify">
  <b>Docker-compose</b> : for creating the elastic-search engine and the interface web-app and link them.
  </p>

- <p align="justify">
  <b>Jupyter</b>:  is an open-source project that provides an interactive computing environment.
  </p>
  
- <p align="justify">
  <b>Pandas</b>:  is a data manipulation library.
  </p>

- <p align="justify">
  <b>pdfplumber</b>: is a pdf manipulation library.
  </p>

- <p align="justify">
  <b>openai</b>: is the Open AI library to their API.
  </p>

- <p align="justify">
  <b>pdfplumber</b>: is a pdf manipulation library.
  </p>
  
- <p align="justify">
  <b>Elastic Search</b>: is a search and analytics engine.
  </p>

- <p align="justify">
  <b>sentence_transformers</b>: is a python library for sentence embeddings.
  </p>

- <p align="justify">
  <b>Plotly Dash</b>: Is a framework for bouilding analytical web application in python.
  </p>
  
## 3. Data Architecture
Diagram of components and expected flow of the project:
<p align="center">
  <img src="images\transit_diagram_architecture_v1.svg">
</p>

Diagram of RAG llm architecture that is used in the project:
<p align="center">
  <img src="images\data_cycle_diagram_v2.svg">
</p>

## 4. Instructions on how to replicate the project
Fortunately all this project version is on a Dockerfile and a docker-compose file, so you can easily copy this project and go to the <code>app_local</code> folder and run the <code>compose.yaml</code> file and enjoy it, please create an .env file with your open ai api key.

```
OPENAI_API_KEY="your key"
```
Inside the <code>app_local</code> are all the files that are needed to run the web-app, there are three .py files <code>dash_interface.py</code> which have the plotly dash code, <code>index_elastic.py</code> which set the elastic search index and <code>rag_functions.py</code> which have all the functions that are used in the rag system, also have the json file used to feed elastic search engine.

you can allways use this command if you don't have experience with docker.
```
docker compose up --build
```
After the conteiners are up please go to the following link to have the web-app ui.
> http://localhost:5080/

You can check if the containers are up using 

```
docker ps
```

<p align="center">
  <img src="images\rag_prueba.png">
</p>

## Future enhancements
- the elastic search part neeeds a better performance, for now it seems to deliver good results but it allways have chance for tunning.
- There are ways to archive better performance of the Rag system, you could combine text+vector to archive better results and/or play with the size of chunk of text to be embedding. Maybe those two steps are going to be things to work to the next version.
- SQLite is used because is easy but it can always be replaced with another RDBMS like postgress, a few lines of code in the docker-compose file and changing the python file.
- I want to migrate this idea to a cloud provider, that will be something to work in a near future.
- Open Ai is NOT cheap if you thing to scalate this, maybe a open-source free llm is a good option. OLLAMA?
- Maybe and just maybe create a better interface for the web-app jejejeje :).
