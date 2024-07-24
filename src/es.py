from elasticsearch import Elasticsearch

# Define the Elasticsearch connection parameters
es = Elasticsearch(hosts=["http://localhost:9200"], api_key="")

# Check if the connection is successful
if es.ping():
    print("Elasticsearch connection is successful.")
else:
    print("Elasticsearch connection failed.")