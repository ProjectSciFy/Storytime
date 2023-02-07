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
# img = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = img['data'][0]['url']
# print(img)