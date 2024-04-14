import json
import requests


employee_data = """
{
  "employees": [
    {"name": "John Smith", "role": "Software Engineer", "years_at_company": 5, "skills": {"languages": ["Python", "Java", "JavaScript"], "technologies": ["AWS", "Linux", "GPT"]}},
    {"name": "Jessica Chen", "role": "UX Designer", "years_at_company": 1, "skills": {"design": ["UI/UX design", "Wireframing", "Prototyping"], "software": ["Adobe XD", "Figma", "Sketch"]}},
    {"name": "Amanda Patel", "role": "Graphic Designer", "years_at_company": 2, "skills": {"design": ["Graphic design", "Typography", "Branding"], "software": ["Adobe Photoshop", "Illustrator", "InDesign"]}},
    ...
  ]
}
""".strip()


def get_user_query():
    return input("Welcome! How can I help you today?: ")


user_query = get_user_query()

stream = False
url = "https://proxy.tune.app/chat/completions"
headers = {
    "Authorization": "nbx_AOyCJtgfpJQnevAvFUiU4mrqL9kB41ZkUAb",
    "Content-Type": "application/json",
}
data = {
  "temperature": 0.8,
    "messages":  [
  {
    "role": "system",
    "content": employee_data 
  },
  {
    "role": "user",
    "content": user_query  
  },
  {
    "role": "assistant"
  }
],
    "model": "rohan/mixtral-8x7b-inst-v0-1-32k",
    "stream": stream,
    "penalty":  0,
    "max_tokens": 900
}
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    json_response = response.json()
   
    answer = json_response['choices'][0]['message']['content']
    print(answer)  
else:
    print("Failed to get a valid response.")
