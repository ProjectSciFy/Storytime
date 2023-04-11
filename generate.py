import helpers as h
import pygame
import requests
from PIL import Image
from io import BytesIO
import openai
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
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="write story on: magic, dragons",
#   max_tokens=1000
# )
# text = response['choices'][0]['text']
# # print(response, text)
# f = open("temp.txt", "a")
# f.write(text)
# f.write("\n---")
# f.close()


# print(h.readTestStories("temp.txt")[0])

'''
IMAGE GENERATION: https://platform.openai.com/docs/guides/images/usage
'''
# img = openai.Image.create(
#   prompt="dog fight cat cartoon",
#   n=1,
#   size="512x512"
# )
# image_url = img['data'][0]['url']
# print(img)

# # Download the image using the requests library
# response = requests.get(image_url)

# # Open the image using the Pillow library
# image = Image.open(BytesIO(response.content))

# # Save the image to disk
# image.save(f"/images/{prompt}{i}.png")

# # Display the image using the Pillow library
# image.show()

def returnToRasa(keywords):
  return " ".join(keywords)

def generateSampleStory(storyNum: int) -> list:
  '''
  storyNum: input integer - 1st story is given by storyNum = 1.
  '''
  storyNumber = storyNum - 1
  s = h.readTestStories("../temp.txt")[storyNumber].split(".")
  text = list()
  images = list()
  # STORY TEXT
  for sentence in s:
    if len(sentence) > 1:
      text.append(sentence.strip() + ".")
      # print(sentence.strip() + ".")
  # STORY IMAGES
  for i, sentence in enumerate(text):
    input = sentence + "cartoon"
    img = openai.Image.create(
      prompt=input,
      n=1,
      size="512x512"
    )
    image_url = img['data'][0]['url']
    # Download the image using the requests library
    response = requests.get(image_url)
    # Open the image using the Pillow library
    image = Image.open(BytesIO(response.content))
    # Save the image to disk
    image.save(f"./images/story_{storyNumber}/sentence_{i}.png")
    images.append(image)
  # FULL STORY
  return (text, images)