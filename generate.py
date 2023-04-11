"""
bug needs to be fixed: i dont have a avalable openai key anymore
can futher add author as input to the generate story '

This code contains functions to generate a story and corresponding images based on given keywords, using the OpenAI text-davinci-003 model and the Dall-E API. 
It also includes a function to insert the generated story and images into an Elasticsearch index.
"""

import helpers as h
import pygame
import requests
from PIL import Image
from io import BytesIO
import openai
import nltk
import os
import elasticSearch 

# Set the OpenAI API key
openai.api_key = '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'

'''
TEXT MODEL OPTIONS: https://platform.openai.com/docs/models/finding-the-right-model
1) text-davinci-003
2) text-curie-001	
3) text-babbage-001	
4) text-ada-001	

IMPORTANT:
https://platform.openai.com/docs/models/content-filter
https://platform.openai.com/docs/guides/moderation/overview
https://platform.openai.com/docs/guides/fine-tuning
'''


def generate_story(keywords):
  """
  Generate a story on the given keywords using the OpenAI text-davinci-003 model.

  Arguments:
  keywords -- A string containing the keywords for the story.

  Returns:
  A string containing the generated story.
  """
  prompt = f"generate a story on: {keywords}"
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=10
  )
  return response.choices[0].text.strip()


def generate_title(story):
  """
  Generate a title for the given story using the OpenAI text-davinci-003 model.

  Arguments:
  story -- A string containing the story.

  Returns:
  A string containing the generated title.
  """
  prompt = f"generate a story title: {story}"
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=5
  )
  return response.choices[0].text.strip()


def generate_images(keywords, image_count):
  """
  Generate a set of images based on the given keywords and image count using the OpenAI Dall-E API.

  Arguments:
  keywords -- A string containing the keywords for the images.
  image_count -- An integer indicating the number of images to generate.

  Returns:
  A list of PIL Image objects containing the generated images.
  """
  try:
    img = openai.Image.create(
      prompt=keywords + " cartoon",
      n=image_count,
      size="512x512"
    )
    return [Image.open(BytesIO(image_bytes)) for image_bytes in img.get("data")]
  except:
    return []


def generateSampleStory(keywords: str) -> list:
  # Generate a story based on the given keywords
  story = generate_story(keywords)

  # Split the story into sentences using the Natural Language Toolkit (nltk)
  sentences = nltk.sent_tokenize(story) if story else []

  # Determine the number of images to generate based on the number of sentences or the number of keywords
  image_count = len(sentences) if sentences else len(keywords.split())

  # Generate a set of images based on the given keywords and image count
  images = generate_images(keywords, image_count)

  # Generate a title for the story using the OpenAI text-davinci-003 model
  storyTitle = generate_title(story)

  # Get the largest story ID in the Elasticsearch index and add 1 to generate a new ID for the current story
  storyNumber = elasticSearch.get_largest_id() + 1

  # Save each generated image to a file
  for i, image in enumerate(images, 1):
    filename = f"./images/story_{storyNumber}/sentence_{i}.png"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename)

  # Set the author name and image folder path for the story, and add it to the Elasticsearch index
  author = "Hans"
  image_folder_path = f"./images/story_{storyNumber}"
  elasticSearch.insert_to_index(keywords, author, storyTitle, story, image_folder_path)

  # Return a list of tuples containing each sentence of the story and its corresponding image
  return [images, sentences]



# if __name__ == "__main__":  
#   generateSampleStory("cat dog cake")

