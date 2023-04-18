"""
This file provides function generateSampleStory(keyword_string, author_name_string)


  generateSampleStory(keywords, author)
    Generate a story based on the given keywords, and save the story and associated images to disk and Elasticsearch.

    Args:
    keywords -- A string containing the keywords for the story.
    author -- A string containing the author name for the story.

    Returns:
    A list containing two elements:
        1. A list of file paths to the generated images.
        2. A list of sentences in the generated story.


    Example usage:
      images, sentences = generateSampleStory("mystery novel", "Jane Doe")
"""

import helpers as h
import pygame
import requests
from PIL import Image
from io import BytesIO
from nltk.tokenize import sent_tokenize
import openai
import nltk
import os
#import elasticSearch 
from math import ceil

# Set the OpenAI API key
openai.api_key = #######
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
  prompt = f"make story on: {keywords}"
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=1000
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
    max_tokens=20
  )
  return response.choices[0].text.strip()


def generate_images(story):
  """
  Generate a set of images based on the given keywords and image count using the OpenAI Dall-E API.

  Arguments:
  keywords -- A string containing the keywords for the images.
  image_count -- An integer indicating the number of images to generate.

  Returns:
  A list of PIL Image objects containing the generated images.
  """
  batches = 0
  image_urls = []

  try:
    while not image_urls:
      batches+=1
      prompts = make_batch_prompt(story, batches)

      for prompt in prompts:
        batch_size = len(nltk.sent_tokenize(prompt))

        if batch_size > 10:
          # the api only accept max size 10 for one batch of generation
          break

        prompt_str = "cartoon " + str(prompt)
        img = openai.Image.create(
          prompt= prompt_str,
          n=batch_size,
          size="512x512"
        )

        # Add the image URLs to the list
        for data in img["data"]:
          image_urls.append(data["url"])
        

    print(image_urls)
    return image_urls
  
  except:
    print("Error generating images")
    return []
  

def make_batch_prompt(story, batches): 
  """
  Tokenizes the given story into individual sentences, and groups them into batches of sentences. Each batch is then
  combined into a paragraph, and a list of paragraphs is returned.

  Args:
    story (str): The story to tokenize and group into batches.
    batches (int): The number of batches to split the sentences into.

  Returns:
    A list of strings, where each string represents a paragraph of sentences.
  """
  # Tokenize the paragraph into individual sentences
  sentences_list = sent_tokenize(story)

  # Calculate how many sentences should be included in each batch
  sentence_per_paragraph = ceil(len(sentences_list) / batches)

  # Create a list of paragraphs, each containing a batch of sentences
  paragraphs = []
  for start_index in range(0, len(sentences_list), sentence_per_paragraph):
    start = start_index
    end = min(len(sentences_list), start_index + sentence_per_paragraph)
    slice_of_sentences = sentences_list[start:end]
    paragraph = ' '.join(slice_of_sentences)
    paragraphs.append(paragraph)

  # Return the list of paragraphs
  return paragraphs


def generateSampleStory(keywords: str, author: str) -> list:
  """
  Generate a story based on the given keywords, and save the story and associated images to disk and Elasticsearch.

  Args:
  keywords -- A string containing the keywords for the story.
  author -- A string containing the author name for the story.

  Returns:
  A list containing two elements:
      1. A list of file paths to the generated images.
      2. A list of sentences in the generated story.
  """
  # Generate a story based on the given keywords
  story = generate_story(keywords).replace("\n", " ").replace("  ", " ")

  # Split the story into sentences using the Natural Language Toolkit (nltk)
  sentences = nltk.sent_tokenize(story) if story else []

  print("this is the sentences ")
  print(sentences)
  print("\n")

  # Generate a set of images based on the given keywords and image count
  images = generate_images(story)

  # Generate a title for the story using the OpenAI text-davinci-003 model
  storyTitle = generate_title(story)

  # Get the largest story ID in the Elasticsearch index and add 1 to generate a new ID for the current story
  #storyNumber = elasticSearch.get_largest_storyNumber() + 1
  storyNumber = 50

  # Save each generated image to a file
  image_folder_path = f"./images/story_{storyNumber}"
  if not os.path.exists(image_folder_path):
    os.makedirs(image_folder_path)

  # Loop over URLs and download/save each image
  image_paths = []
  for i, url in enumerate(images):
      response = requests.get(url)
      image_paths.append(f"{image_folder_path}/sentence_{i}.png")
      with open(f"{image_folder_path}/sentence_{i}.png", "wb") as f:
          f.write(response.content)

  # Set the author name and image folder path for the story, and add it to the Elasticsearch index
  #elasticSearch.insert_to_index(keywords, author, storyTitle, story, image_folder_path)

  # Return a list of tuples containing each sentence of the story and its corresponding image
  print(image_paths)
  return [image_paths, sentences, storyNumber]



# for testing purpose
# if __name__ == "__main__":  
#   generateSampleStory("sneeze cat jacket", "Gal Pinhasi")
      



