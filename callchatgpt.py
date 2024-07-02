import os
import subprocess
from openai import AzureOpenAI
from environment import endpoint,tok
import requests
import base64
from azure.identity import DefaultAzureCredential, get_bearer_token_provider



os.environ['AZURE_OPENAI_ENDPOINT'] = endpoint
os.environ['AZURE_OPENAI_API_KEY'] = tok

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

with open('./Onion.jfif')

response = client.chat.completions.create(
    model="gpt-4o", # model = "deployment_name".
    messages=[
        {"role": "system", "content": [
            {"type": "text", 
             "text": "You are a helpful assistant."}
            ]},
        {"role": "user", "content": [{
            "type": "image_url",
            "image_url":{
                "url":image
            }
        },
        {"type":"text",
         "text":"Describe this image"}
      ]
    }
  ]
)

print(response.choices[0].message.content)

# Configuration
# GPT4V_KEY = os.getenv("AZURE_OPENAI_API_KEY")
# IMAGE_PATH = "C:/Users/angj02/OneDrive - FrieslandCampina/Desktop/test/Onion.jfif"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
# headers = {
#     "Content-Type": "application/json",
#     "api-key": GPT4V_KEY,
# }

# # Payload for the request
# payload = {
#   "messages": [
#       {"role": "system", "content": "You are a helpful assistant."},
#       {"role": "user", "content": "Describe the picture"}
#   ],
#   "temperature": 0.7,
#   "top_p": 0.95,
#   "max_tokens": 800
# }

# GPT4V_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

# # Send request
# try:
#     response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
#     response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
# except requests.RequestException as e:
#     raise SystemExit(f"Failed to make the request. Error: {e}")

# # Handle the response as needed (e.g., print or process)
# print(response.json())
