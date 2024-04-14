import requests
import os
from groq import Groq
import json


GROQ_API_KEY='x'

# Correct the environment variable name and use quotes
client = Groq(
    api_key=os.environ.get(GROQ_API_KEY),
)

def augment_prompt(query: str):
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{"query": [    {      "query": "{query_from_user}",      "queryContext": "",      "start": 0,      "numResults": 10,      "contextConfig": {        "charsBefore": 0,        "charsAfter": 0,        "sentencesBefore": 2,        "sentencesAfter": 2,        "startTag": "%START_SNIPPET%",        "endTag": "%END_SNIPPET%"      },      "corpusKey": [        {          "customerId": 2531807925,          "corpusId": 3,          "semantics": 0,          "metadataFilter": "doc.id = \'California-Tenants-Guide.pdf\'",          "lexicalInterpolationConfig": {            "lambda": 0.025          },          "dim": []        }      ],      "summary": [        {          "debug": false,          "maxSummarizedResults": 5,          "responseLang": "eng",          "summarizerPromptName": "vectara-summary-ext-v1.2.0",          "factualConsistencyScore": true        }      ]    }  ]}END        '
    response = requests.post('https://api.vectara.io:443/v1/stream-query', headers=headers, data=data)
    response.content
    print(response.content)

    # feed into an augmented prompt
    augmented_prompt = f""" 
    You are an California Tenant Law Expert. 
    Using the contexts below, answer the query. 
    Make sure to give a well-structed response. 
    Use clear speech that is understandable. Be sure to answer anlytically
    Temperature = 0.2 
    Also Make sure to specifically cite all the resources and add the links to the respective locations where you found the information in your resources (the vector data base)!
    Ensure that they are usable
    Always act as you are speaking directly to the user/landlord/tenant and at a citation from the resources where you obtained your RAG information.

    Contexts:
    {response.content}

    Query: {query}"""
    return augmented_prompt

def get_query_from_user(query: str):
    augmented_prompt = augment_prompt(query)
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": augmented_prompt,
        }
    ],
    model="mixtral-8x7b-32768",
    )
    result=chat_completion.choices[0].message.content

    return result