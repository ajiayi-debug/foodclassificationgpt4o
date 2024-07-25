# Instructions to set up openai api with azure ai (As of 18/7/2024)
## Installing dependencies
To start, install the required packages:

```sh
pip install -r requirements.txt
```

## Get access to openai group ad-group as well as install Azure cli tool
### Accessing Azure CLI:
Download Azure CLI from [azure cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)
### Finding Azure CLI:
This part is only necessary if your device cannot find the path to Azure CLI. 

Go to CMD and type `where az`.

Take note of the path with `./az.cmd`. You will need this path to create your .env file

## Finding token and endpoint
Token will automatically be created when running any .py files in /src while endpoint can be found in Azure AI Studios/ Resources and Keys/ Resource name/ </> View Code

## Finding version
Take note that the prompt format only works for gpt 4 onwards (only can recognise images with gpt 4 onwards). Replace [model] with gpt version. In my case, I used "gpt-4o". Replace [version] with your version of model. This can be found in Azure AI Studios/ Resources and Keys/ Deployments/ name of model. In my case, I used "2024-02-01"

## Certificate issues
I personally had no issues with the certificate (I just downloaded the certificate). However, if you do face issues, insert the path to certificate into [path to certificate]

## Create .env file in main directory
Replace [endpoint], [path to certificate], [version], [model] and [az cli] with the respective links and paths

```
endpoint = [endpoint]
az_path = [az cli]
ver=[version]
cert=[path to certificate]
name=[model]
```

## How to run
### Food classification
Run any of the .py files in src to run food classification. Change the image relative path to test different images in
```
base64image=encode_image([image relative path])
```
