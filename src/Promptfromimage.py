import os
import subprocess
from openai import AzureOpenAI
from dotenv import load_dotenv
import requests
import base64
from azure.identity import DefaultAzureCredential

load_dotenv()
az_path = os.getenv("az_path")

# Fetch Azure OpenAI access token
result = subprocess.run([az_path, 'account', 'get-access-token', '--resource', 'https://cognitiveservices.azure.com', '--query', 'accessToken', '-o', 'tsv'], stdout=subprocess.PIPE)
token = result.stdout.decode('utf-8').strip()

# Set environment variables
os.environ['AZURE_OPENAI_ENDPOINT'] = os.getenv('endpoint')
os.environ['AZURE_OPENAI_API_KEY'] = token


# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("ver")
)

# Read and encode the image file
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("./stirrednoods.jfif") #can be image url as well


# Create a completion request
response = client.chat.completions.create(
    temperature=0,
    model="gpt-4o",  # Adjust the model name as needed
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": [
            #Can you quantify the ingredients and estimate the respective micronutrients by estimating and calculating the volume of the food in the picture? Use the picture only (no external recipes, just use what you see in the picture and no average size).Include Sodium,Vitamins and Macronutrients. and also give me a classification of what food it is. Format your answer according to this : Food name, then nutrients. why do you think the meat is what it is from the picture
            {"type": "text", "text": "Can you quantify the ingredients and estimate the respective micronutrients by estimating and calculating the volume of the food in the picture? Use the picture only (no external recipes, just use what you see in the picture and no average size).Include Sodium,Vitamins and Macronutrients and also give me a classification of what food it is. Format your answer according to this : Food name, then nutrients. Why do you think the food and ingredients is what it is?"},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ]
)

# Print the response
print(response.choices[0].message.content)

