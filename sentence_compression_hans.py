# https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/summarization/quickstart?tabs=document-summarization&pivots=programming-language-python
# https://portal.azure.com/#@buckeyemail.osu.edu/resource/subscriptions/138c471a-6ebc-40d2-bb27-014c71c03aae/resourceGroups/hanscapstone/providers/Microsoft.CognitiveServices/accounts/hanscapstone/cskeys

# this file is testing the smmarize result for the story  

key = "bed2fcd6ac06464989b9dd71f5d0c382"
endpoint = "https://hanscapstone.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint  
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for summarizing text
def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractSummaryAction
    ) 

    document = [
    "One day, while Pip was scurrying through the forest, she stumbled upon a large black dog named Max. Max was a friendly dog who loved to chase after squirrels and play fetch with his owner."
    "At first, Pip was frightened of Max. She had heard stories of dogs chasing and killing mice. But as she watched Max, she noticed something different about him. He didn't seem interested in chasing or hurting her. Instead, he wagged his tail and looked at her with kind eyes." 
    "Pip cautiously approached Max, and to her surprise, he welcomed her with a wag of his tail. From that moment on, Pip and Max became the best of friends. They would play together in the forest, with Max always careful not to hurt Pip with his big paws."
    "As they explored the forest together, Pip and Max encountered many adventures. They discovered hidden caves, climbed tall trees, and swam in the crystal clear streams. Pip was always amazed at how fearless Max was, and Max loved having Pip by his side to share in his adventures."
    "Even though they were different species, Pip and Max had a bond that was unbreakable. They were the best of friends, and nothing could ever come between them."
    "And so, Pip and Max continued to explore the magical forest together, living out their days in the purest form of friendship that could ever exist."
    ]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractSummaryAction(max_sentence_count=4)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )

sample_extractive_summarization(client)