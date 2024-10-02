FROM python:3.11.9
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY dash_interface.py dash_interface.py
COPY rag_functions.py rag_functions.py
COPY index_elastic.py index_elastic.py
COPY documents-with-ids.json documents-with-ids.json
EXPOSE 8050
CMD [ "bash","-c","python index_elastic.py && python dash_interface.py" ]