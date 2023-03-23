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

def generate_text(input1, input2, input3, input4): 
    prompt_sentence = f"write short story on: {input1}, {input2}, {input3}, {input4}"
    print(prompt_sentence)
    response = openai.Completion.create(
        model="text-curie-001",
        #prompt="write a ten sentence story about: magic and dragons",
        prompt=prompt_sentence,
        max_tokens=1000
    )
    text = response['choices'][0]['text']
    print(response, text)
    return text

#generate_text('dragons', 'magic', 'dinasours', 'dolphins')
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