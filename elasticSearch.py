"""
This code connects to an Elasticsearch instance hosted in Elastic Cloud, creates an index, inserts data into the index, retrieves data from the index, and loads JSON data into the index.

POST
    insert_to_index(query_sentence, author, title, content, image_folder_path)  
        Inserts data into the Elasticsearch index with the specified fields.
        Arguments:
            query_sentence (str)
            author (str)
            title (str)
            content (str)
            image_folder_path (str)

GET
    query_story_by_storyNumber(storyNumber)
        Queries Elasticsearch for a story with the specified storyNumber and returns its contents.
        Arguments:
            storyNumber (int)

DELETE
    delete_story_by_storyNumber(storyNumber)
        Deletes a story from Elasticsearch based on its storyNumber.
        Arguments:
            storyNumber (int)

Others:
    connect_elasticsearch()
        Connects to the Elasticsearch instance and returns a client object.

    create_index()
        Creates an Elasticsearch index with the specified name, settings, and mappings.

    print_all_data()
        Retrieves all data from the Elasticsearch index and prints it.

    load_json_data()
        Loads data from a JSON file and indexes it into the Elasticsearch index. Example data is in example_data.json.

    get_titles_from_es()
        Connects to Elasticsearch and retrieves the titles of all stories in the index. Returns a list of title strings.

    search_story_by_title(title)
        Connects to Elasticsearch and searches for a story with the specified title.
        If a single story is found, returns a tuple containing a list of image paths for each sentence in the story and a list of sentences in the story. If no story is found, prints an error message and returns empty lists.
        Arguments:
            title (str)

"""

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import nltk
import json
from nltk.tokenize import sent_tokenize

CLOUD_ID = "StoryTime:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRhYjRkMWU4OWNjMzY0YjBhYTRhZmQ4ZmYzYjY0ZjBhMCQ2ZGQ4NjlkNDg1YmY0M2Y0OTdjYzVkODMwMDY1ODM5NA=="
USERNAME = "elastic"
PASSWORD = "6TOzjl21shgOowUz46ONFKCB"
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
                "storyNumber": {
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

def query_story_by_storyNumber(storyNumber):
    """
    This function queries Elasticsearch for a story with the specified storyNumber and returns its contents.
    """
    client = connect_elasticsearch()
    index_name = INDEX_NAME

    query = {
        "query": {
            "match": {
                "storyNumber": storyNumber
            }
        }
    }
    res = client.search(index=index_name, body=query)
    hits = res['hits']['hits']
    # print(type(hits[0]['_source']['storyNumber']))

    if hits:
        print(hits[0]['_source'])
        return hits[0]['_source']
    else:
        return None



def delete_story_by_storyNumber(del_storyNumber):
    """
    This function deletes a story from Elasticsearch based on its storyNumber
    """
    client = connect_elasticsearch()
    index_name = INDEX_NAME

    query = {
        "query": {
            "match": {
                "storyNumber": del_storyNumber
            }
        }
    }
    
    try:
        client.delete_by_query(index=index_name, body=query)
        print(f"Delete story with storyNumber {del_storyNumber}")
    except NotFoundError:
        print(f"Story with storyNumber {del_storyNumber} not found")
    except Exception as e:
        print(f"Error deleting story with storyNumber {del_storyNumber}: {e}")
    


def get_largest_storyNumber():
    """
    Searches for the largest storyNumber in the Elasticsearch index.
    Returns:
        The largest storyNumber found in the Elasticsearch index.
    """
    client = connect_elasticsearch()
    index_name = INDEX_NAME

    # Search for the largest storyNumber
    search_query = {
        "query": {
            "match_all": {}
        },
        "sort": [
            {
                "storyNumber": {
                    "order": "desc"
                }
            }
        ]
    }
    result = client.search(index=index_name, body=search_query, size=1)
    hits = result.get("hits", {}).get("hits", [])
    if hits:
        largest_storyNumber = hits[0]["_source"].get("storyNumber", 0)
    else:
        largest_storyNumber = 0

    return largest_storyNumber


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

    # Get the largest storyNumber
    largest_storyNumber = get_largest_storyNumber()
    storyNumber = largest_storyNumber + 1

    storyNumber = int(storyNumber)
    query_sentence = str(query_sentence)
    author = str(author)
    title = str(title)
    content = str(content)
    image_folder_path = str(image_folder_path)

    item = {
        "storyNumber": storyNumber,
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
                'storyNumber': item['storyNumber'],
            }
        }
        source_data = item
        actions.append(action)
        actions.append(source_data)

    # use the bulk API to index the data
    response = client.bulk(index=index_name, body=actions, refresh=True)
    print(response)


def get_titles_from_es():
    client = connect_elasticsearch()
    index_name = INDEX_NAME

    # Define the search query
    search_query = {
        "query": {
            "match_all": {}  # Retrieve all documents
        },
        "_source": ["story.title"]  # Only return the title field
    }

    # Execute the search query
    response = client.search(index=index_name, body=search_query)

    # Extract the titles from the response
    titles = [hit["_source"]["story"]["title"] for hit in response["hits"]["hits"]]

    return titles

from elasticsearch import Elasticsearch


def search_story_by_title(title):
    client = connect_elasticsearch()  # assuming you have already defined this function
    index_name = INDEX_NAME  # assuming you have already defined this variable

    sentences = []
    image_paths = []

    # Define the search query
    search_query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"story.content": title}}
                ],
                "filter": [
                    {"match_phrase": {"story.title": {"query": title, "slop": 0}}}
                ]
            }
        }
    }

    # Execute the search query
    response = client.search(index=index_name, body=search_query)

    # Extract the story content from the response
    if response["hits"]["total"]["value"] == 1:  # Check if only one story is found
        story_content = response["hits"]["hits"][0]["_source"]["story"]["content"]
        image_folder = response["hits"]["hits"][0]["_source"]["image_folder_path"]
        sentences = nltk.sent_tokenize(story_content)
        
        #generate the image_path
        for i in range(len(sentences)):
            image_paths.append(f"{image_folder}/sentence_{i}.png")

        # print(len(image_paths), len(sentences))
        return [image_paths, sentences]
    else:
        print("No story found with title '{}'".format(title))
        return [image_paths, sentences]
    


# if __name__ == "__main__":   
    # create_index()
     
    # query_sentence = "generate a story the talks about pig honey and bear"
    # title = "The Unlikely Friendship of a Pig, a Honeybee, and a Bear"
    # content = "Once upon a time, deep in the heart of a lush forest, there lived a pig named Percy. Percy was a friendly pig who loved to roam around the forest in search of tasty treats. One day, while exploring the woods, he stumbled upon a beehive filled with golden honey. Percy couldn't resist the sweet aroma of the honey and decided to help himself to a taste. As he was savoring the delicious honey, a large bear named Bruno appeared out of nowhere. Bruno was known throughout the forest for his love of honey and his fierce nature. Percy, realizing he was caught in the act, braced himself for an angry confrontation with Bruno. But to his surprise, Bruno wasn't angry at all. Instead, he asked Percy where he had found the honey. Percy, realizing he had nothing to lose, led Bruno to the beehive where he had discovered the honey. Bruno was overjoyed and thanked Percy for showing him the way. Together, they feasted on the honey, savoring every last drop. As they ate, they chatted and got to know each other better. Percy discovered that Bruno wasn't as fierce as he had originally thought. In fact, Bruno had a soft spot for pigs like Percy. They shared stories about their adventures in the forest and laughed about their silly mishaps. From that day on, Percy and Bruno became the best of friends. They would meet regularly at the beehive and enjoy honey together, always remembering the day they first met. And so, in the heart of the forest, a pig and a bear became unlikely friends over their shared love of honey."
    # author = "Ellie Henkaline" 
    # image_folder_path = "/home/user/images/story6"

#     insert_to_index(query_sentence, author, title, content, image_folder_path)

    # print_all_data()
    # for i in range (6, get_largest_storyNumber()):
    # query_story_by_storyNumber(1)
    # delete_story_by_storyNumber(1)  
        
    # print(get_largest_storyNumber())
    # print(query_story_by_storyNumber(1))
    # print(get_largest_storyNumber())


    # print(get_titles_from_es())
    # res = get_titles_from_es()
    # print(search_story_by_title(res[0]))

