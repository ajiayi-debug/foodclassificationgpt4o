import os
import subprocess
from openai import AzureOpenAI
from environment import endpoint,tok
import requests
import base64
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

os.environ['AZURE_OPENAI_ENDPOINT'] = endpoint
os.environ['AZURE_OPENAI_API_KEY'] = tok

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01"
)

# Read and encode the image file
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("puppy.jfif") #can be image url as well


# Create a completion request
response = client.chat.completions.create(
    model="gpt-4o",  # Adjust the model name as needed
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": [
            {"type": "text", "text": "Describe the image"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ]
)

# Print the response
print(response.choices[0].message.content)

