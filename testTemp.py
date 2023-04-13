import helpers as h
import pygame
import requests
from PIL import Image
from io import BytesIO
import openai
from math import ceil

# import nltk
from nltk.tokenize import sent_tokenize
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

# '''
# IMAGE GENERATION: https://platform.openai.com/docs/guides/images/usage
# '''
image_urls = []
# img = openai.Image.create(
#   prompt="Generate pictures for story: Once upon a time there was a little boy who loved to take the tests at school. He was a smart student, and he always made sure to use a special pencil when it was time for the test. The pencil was old and had been passed down from generation to generation. It was said to have been made by a ghost long ago. No one knew exactly how long the pencil had been around, but it seemed like forever.",
#   n=3,
#   size="512x512"
# )
# for data in img["data"]:
#     image_urls.append(data["url"])

# print(image_urls)




# # Download the image using the requests library
# response = requests.get(image_url)

# # Open the image using the Pillow library
# image = Image.open(BytesIO(response.content))

# # Save the image to disk
# image.save(f"/images/{prompt}{i}.png")

# # Display the image using the Pillow library
# image.show()


story = "Once upon a time, there was a student, Emma, who had a difficult test penciled in for the next day. She had been studying hard, but she was a little nervous about the exam. As the time came closer to the test, Emma began to worry more and more. She grabbed her trusty pencil and began to practice her test material, filling page after page on her practice exam. However, as Emma was writing on one of her practice tests she noticed, to her surprise, that an errant pencil had gone across one of her questions and left a ghostly imprint. She looked up from her paper in disbelief, wondering how the pencil got there. But as soon as she put the pencil down, an eerie chill swept across the room, and the ghostly pencil moved all on its own. Emma stared at the pencil in shock and then, a few seconds later, the ghost pencil returned to its place on her practice paper and the ghostly goast disappeared, leaving only the faint imprint it had left behind. The next day, as Emma arrived at her testing center, she was much more prepared and confident. She smiled as she smoothly wrote out her answers, and soon the test was over. Amazingly, Emma passed with flying colors, and she knew that her faithful test pencil ghost had a lot to do with her success. From that day forward, Emma dedicated more time to her studies and never again did she have to worry about another test pencil goast showing up again."
















# text = "Once upon a time, there was a little girl called Alice who was very creative and loved to draw. Every day after school she would sit in her room and create art with her pencil. One day, while Alice was drawing, she noticed something very strange. The pencil she was using began to move by itself! She was so surprised and a bit scared that it might be a ghost. But no matter how much she watched it, the pencil would not stop moving. Alice decided to confront the pencil ghost. She stared at it and said, “Who are you?” Immediately the pencil ghost spoke. It said, “I am the Test Pencil Ghost. I have been stuck in this pencil for countless years waiting for someone to find me. Now I’m finally free!” Alice was amazed by this and asked the ghost if it could help her with her art. The ghost said it would be delighted to help her create amazing artworks. Alice and the Test Pencil Ghost worked together for many years, creating beautiful pieces of art. After years of hard work, Alice eventually became a famous artist. Whenever she was asked how she achieved her success, she would always reply with a smile, “Thanks to my Test Pencil Ghost.”"

# i = 4  # Set the number of paragraphs

# # Tokenize the paragraph into individual sentences
# sentences_list = sent_tokenize(text)

# sentence_per_paragraph = ceil(len(sentences_list) / i)

# paragraphs = []
# for j in range(0, len(sentences_list), sentence_per_paragraph):
#     start = j
#     end = min(len(sentences_list), j + sentence_per_paragraph)
#     slice_of_sentences = sentences_list[start:end]
#     paragraph = ' '.join(slice_of_sentences)
#     paragraphs.append(paragraph)

# print(len(paragraphs))
# print(paragraphs)

