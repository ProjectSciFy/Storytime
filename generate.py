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
#   model="text-curie-001",
#   prompt="write a short story about: magic and dragons",
#   max_tokens=50
# )
# text = response['choices'][0]['text']
# print(response, text)

'''
IMAGE GENERATION: https://platform.openai.com/docs/guides/images/usage
'''
img = openai.Image.create(
  prompt="generate cartoon style pictures with this story: One day, while Pip was scurrying through the forest, she stumbled upon a large black dog named Max. Max was a friendly dog who loved to chase after squirrels and play fetch with his owner. At first, Pip was frightened of Max. She had heard stories of dogs chasing and killing mice. But as she watched Max, she noticed something different about him. He didn't seem interested in chasing or hurting her. Instead, he wagged his tail and looked at her with kind eyes. Pip cautiously approached Max, and to her surprise, he welcomed her with a wag of his tail. From that moment on, Pip and Max became the best of friends. They would play together in the forest, with Max always careful not to hurt Pip with his big paws.As they explored the forest together, Pip and Max encountered many adventures.",
  n=5,
  size="1024x1024"
)
image_url = img['data'][0]['url']
print(img)