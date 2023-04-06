"""
BUG LEFT: FIX THE image_folder_path


This code connects to an Elasticsearch instance hosted in Elastic Cloud, creates an index, 
inserts data into the index, retrieves data from the index, and loads JSON data into the index.
    

POST
    insert_to_index(query_sentence, author, title, content, image_folder_path)  
        Inserts data into the Elasticsearch index with the specified fields.
        Arguments:
            query_sentence
                type: string
            author
                type: string
            title
                type: string
            content
                type: string 
            image_folder_path
                type: string

GET
    query_story_by_id(id)
        queries Elasticsearch for a story with the specified ID and returns its contents.
        type: int

DELETE
    delete_story_by_id(id)
        deletes a story from Elasticsearch based on its ID
        type: int


others:
    connect_elasticsearch()
        connects to the Elasticsearch instance and returns a client object.

    create_index()
        creates an Elasticsearch index with the specified name, settings, and mappings.

    print_all_data()
        retrieves all data from the Elasticsearch index and prints it.

    load_json_data()
        loads data from a JSON file and indexes it into the Elasticsearch index.
        example data is in example_data.json

"""

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import json

CLOUD_ID = "23d32ecdc6f74baeacef270609a9f7b9:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDRiZjMwZjg4NTY5MTQzMjI5MjZiN2ZhNWRhZGMzOWY1JDlkZWVlOGNhNGM0NDQ4NWFiZDRlMTI5N2MyOGVhN2I1"
USERNAME = "elastic"
PASSWORD = "M8T3yNGiPxmGNDO4mDhWnyxs"
INDEX_NAME = "storytime_index"

def connect_elasticsearch():
    """
    Connects to an Elasticsearch instance hosted in Elastic Cloud and returns a client object.
    """
    client = Elasticsearch(
        cloud_id= CLOUD_ID,
        http_auth=(USERNAME, PASSWORD)
    )
    
    client.info()

    if client.ping():
        print("Connected to Elastic Cloud")
    else:
        print("Connection failed")

    return client


def create_index():
    """
    Creates an Elasticsearch index with the specified name, settings, and mappings.
    """
    client = connect_elasticsearch()
    index_name = INDEX_NAME

    if client.indices.exists(index=index_name):
        print(f"Index '{index_name}' already exists, skipping creation.")
        return
        
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "keywords": {
                    "properties": {
                        "query_sentence": {
                            "type": "text"
                        }
                    }
                },
                "story": {
                    "properties": {
                        "title": {
                            "type": "text"
                        },
                        "author": {
                            "type": "text"
                        },
                        "content": {
                            "type": "text"
                        }
                    }
                },
                "image_folder_path": {
                    "type": "text"
                }
            }
        }
    }


    client.indices.create(index=index_name, body=settings)
    print(client.indices.get(index=index_name))

def query_story_by_id(id):
    """
    This function queries Elasticsearch for a story with the specified ID and returns its contents.
    """
    client = connect_elasticsearch()
    index_name = INDEX_NAME

    try:
        res = client.get(index=index_name, id=id)
        return res["_source"]
    except NotFoundError:
        print(f"Story with ID {id} not found")
        return None


def delete_story_by_id(id):
    """
    This function deletes a story from Elasticsearch based on its ID
    """
    client = connect_elasticsearch()
    index_name = INDEX_NAME
    
    try:
        client.delete(index=index_name, id=id)
        print(f"Deleted story with id {id}")
    except NotFoundError:
        print(f"Story with id {id} not found")
    except Exception as e:
        print(f"Error deleting story with id {id}: {e}")
    


def insert_to_index(query_sentence, author, title, content, image_folder_path):
    """
    Inserts data into the Elasticsearch index with the specified fields.
        Arguments:
            query_sentence
                ->this should be a string that stores the query sentence that user used to create the story ex: Create a story about cake, cat and magic
            author
                ->this stores a string of the authors name ex: Hans Yu
            title
                ->stores a string the contains the title of the story ex "Magic cat who likes cake"
            content
                ->stores a string of the whole story 
            image_folder_path
                -> stores the path that stores the path of this story
    """

    client = connect_elasticsearch()
    index_name = INDEX_NAME

    #get the largest id in the elasticSearch index
    search_query = {
        "query": {
            "match_all": {}
        },
        "sort": [
            {
                "id": {
                    "order": "desc"
                }
            }
        ]
    }
    result = client.search(index=index_name, body=search_query, size=1)
    largest_id = result['hits']['hits'][0]['_source']['id']
    if not largest_id:
        largest_id = 1
    else:  
        largest_id = largest_id + 1

    id = largest_id

    item = {
        "id": id,
        "keywords": {
            "query_sentence": query_sentence
        },
        "story": {
            "title": title,
            "author": author,
            "content": content
        },
        "image_folder_path": image_folder_path
    }
    result = client.index(index=index_name, body=item)
    print(result)


def print_all_data():
    client = connect_elasticsearch()
    index_name = INDEX_NAME
    result = client.search(index=index_name, body={"query": {"match_all": {}}})
    for hit in result['hits']['hits']:
        print(hit['_source'])
        print('\n')


def load_json_data():
    client = connect_elasticsearch()
    index_name = INDEX_NAME
    with open('example_data.json') as f:
        data = json.load(f)
    
    actions = []
    for item in data:
        action = {
            'index': {
                '_index': index_name,
                '_id': item['id'],
            }
        }
        source_data = item
        actions.append(action)
        actions.append(source_data)

    # use the bulk API to index the data
    response = client.bulk(index=index_name, body=actions, refresh=True)
    print(response)


if __name__ == "__main__":   
#     create_index()
     
#     query_sentence = "generate a story the talks about pig honey and bear"
#     title = "The Unlikely Friendship of a Pig, a Honeybee, and a Bear"
#     content = "Once upon a time, deep in the heart of a lush forest, there lived a pig named Percy. Percy was a friendly pig who loved to roam around the forest in search of tasty treats. One day, while exploring the woods, he stumbled upon a beehive filled with golden honey. Percy couldn't resist the sweet aroma of the honey and decided to help himself to a taste. As he was savoring the delicious honey, a large bear named Bruno appeared out of nowhere. Bruno was known throughout the forest for his love of honey and his fierce nature. Percy, realizing he was caught in the act, braced himself for an angry confrontation with Bruno. But to his surprise, Bruno wasn't angry at all. Instead, he asked Percy where he had found the honey. Percy, realizing he had nothing to lose, led Bruno to the beehive where he had discovered the honey. Bruno was overjoyed and thanked Percy for showing him the way. Together, they feasted on the honey, savoring every last drop. As they ate, they chatted and got to know each other better. Percy discovered that Bruno wasn't as fierce as he had originally thought. In fact, Bruno had a soft spot for pigs like Percy. They shared stories about their adventures in the forest and laughed about their silly mishaps. From that day on, Percy and Bruno became the best of friends. They would meet regularly at the beehive and enjoy honey together, always remembering the day they first met. And so, in the heart of the forest, a pig and a bear became unlikely friends over their shared love of honey."
#     author = "Ellie Henkaline" 
#     image_folder_path = "/home/user/images/story6"

#     insert_to_index(query_sentence, author, title, content, image_folder_path)

    print_all_data()

    # print(get_largest_id())
    # print(query_story_by_id(1))
