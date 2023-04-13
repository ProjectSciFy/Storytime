"""
ONE BUG LEFT: FIX THE image_folder_path

This python code provide functions to connect to mongoDB
There are two functions provided

   insert_to_db(query_sentence, author, title, content, image_folder_path)
      purpose: this function insert the story to the database
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

         
   query_story_by_ID(storyID)
      purpose: this function search the story in the database by storyID
      Arguments:
         storyID
            -> a interger that generates when inserted into the database
            
"""
import os
from pymongo import MongoClient
import pymongo

from dotenv import load_dotenv

load_dotenv() # Load environment variables from the .env file

DATABASE_NAME = 'StoryTime'
STORIES_COLLECTION_NAME = 'story_time_data'
CONNECTION_STRING =  os.environ.get('MONGODB_CONNECTION_STRING')

def get_database():
   """Connect to the MongoDB Atlas instance and return the StoryTime database object."""
   connection_string = CONNECTION_STRING
   client = MongoClient(connection_string)
   return client[DATABASE_NAME]

def insert_to_db(query_sentence, author, title, content, image_folder_path):
   """Insert a new story document into the MongoDB database."""
   db = get_database()
   collection = db[STORIES_COLLECTION_NAME]

   #find an avaliable ID 
   document = collection.find_one(sort=[("id", pymongo.DESCENDING)])
   if document is None:
      id = 1
   else:
      id = document["id"] + 1

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

   db = get_database()
   collection = db[STORIES_COLLECTION_NAME]
   
   try:
      result = collection.insert_one(item)
      return result.inserted_id
   except pymongo.errors.PyMongoError as e:
      raise Exception("Error inserting story: {}".format(str(e)))


def query_story_by_id(story_id):
   """Query the database for a story document with the given ID."""
   db = get_database()
   collection = db[STORIES_COLLECTION_NAME]

   result = collection.find_one({"id" : story_id})
   if result is None:
      return None
   else:
      return result["story"]["content"]

