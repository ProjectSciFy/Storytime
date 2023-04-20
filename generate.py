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
from openai.error import OpenAIError
import nltk
import os
# import elasticSearch 
from math import ceil

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
  prompt = f"generate short story title: {story}"
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=20
  )
  return response.choices[0].text.strip()


def generate_images(story, batches):
  """
  Generate a set of images based on the given keywords and image count using the OpenAI Dall-E API.

  Arguments:
  keywords -- A string containing the keywords for the images.
  image_count -- An integer indicating the number of images to generate.

  Returns:
  A list of PIL Image objects containing the generated images.
  """
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

        prompt_str = f"cartoon {str(prompt)}"
        img = openai.Image.create(
          prompt= prompt_str,
          n=batch_size,
          size="512x512"
        )

        # Add the image URLs to the list
        for data in img["data"]:
          image_urls.append(data["url"])
        

    print(image_urls)
    print(len(image_urls), len(sent_tokenize(story)))
    return image_urls

  except OpenAIError as e:
    print(f"Batchs = {batches}. Error generating images: {e}")
    if "is too long - 'prompt'" in str(e):
      generate_images(story, batches)
    else:
      return image_urls

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
  # storyNumber = elasticSearch.get_largest_storyNumber() + 1
  storyNumber = 1

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
  # elasticSearch.insert_to_index(keywords, author, storyTitle, story, image_folder_path)

  # Return a list of tuples containing each sentence of the story and its corresponding image
  print(image_paths)
  return [image_paths, sentences]



# for testing purpose
# if __name__ == "__main__":  
#   generateSampleStory("car teeth bear", "Hans Yu")

    # There are words in the story that openAi doesn't allow image generation api generate image
    # story = "Once upon a time, in a galaxy far, far away, the Jedi Lightsaber Empire ruled with an iron fist. For centuries, they were the undisputed rulers of the galaxy, and their mysterious lightsabers of immense power were the cornerstone of their reign. However, a small but determined group of insurgents soon rose up against the Empire’s might. Like a wildfire, word of rebellion soon spread, and a great number of diverse races and factions joined forces to challenge the Empire’s oppression. The Empire sent waves of reinforcements to repel the insurgency, but these reinforcements were no match for the warriors wielding the powerful lightsabers. These stalwart rebels slowly chipped away at the Empire’s prided control of the galaxy and eventually, through sheer strength of will, managed to rid the galaxy of Empire's oppressive rule and restored peace and freedom. And so, the Rebellion achieved victory, due in part to their courage, but also thanks to their mastery of the lightsaber technology. The weapon would remain an enduring part of the galaxy and a symbol of hope for all the oppressed, reminding them that together, anything was possible."
    # story = "Once upon a time, in a galaxy far, far away, the Jedi Lightsaber Empire ruled with an iron fist. For centuries, they were the undisputed rulers of the galaxy, and their mysterious lightsabers of immense power were the cornerstone of their reign. However, a small but determined group of insurgents soon rose up against the Empire’s might. Like a wildfire, word of rebellion soon spread, and a great number of diverse races and factions joined forces to challenge the Empire’s oppression."
    # story = "Once upon a time, in a galaxy far, far away, the Jedi Lightsaber Empire ruled with an iron fist."
    # story = "Once upon a time, in a galaxy far, far away."
    
    # story = "In a world far different from our own, there existed a great kingdom ruled by a benevolent queen. This kingdom was a place of peace and prosperity, where every citizen was treated with kindness and respect.However, as is often the case, there were those who coveted the queen's power and sought to overthrow her. They formed a secret society, known only as the Black Hand, and began to spread their influence throughout the kingdom.At first, their actions were subtle and difficult to detect. They whispered lies and half-truths in the ears of the people, slowly turning them against their beloved queen. But as their power grew, so too did their ambition.Soon, the Black Hand had amassed a vast army of followers and launched a full-scale assault on the kingdom. The queen, determined to protect her people and her throne, called upon her most trusted advisors to form a plan of defense.They devised a strategy that would rely on a group of highly-skilled warriors known as the Silver Blades. These warriors were the best of the best, and they wielded magical swords that were said to be imbued with the power of the gods themselves.The Silver Blades accepted the queen's call to action and set out to face the Black Hand's army head-on. The battle was long and grueling, but in the end, the Silver Blades emerged victorious. The Black Hand was defeated, and the kingdom was saved from certain destruction. In honor of the Silver Blades' bravery, the queen granted them a special status within the kingdom. They were no longer mere warriors, but were instead regarded as heroes and protectors of the realm. And so, the kingdom lived on in peace and prosperity, with the Silver Blades standing ever-vigilant against any who would dare to threaten their way of life."
    # print(generate_images(story, 0))


