# You can read about the new Python Azure AI Inference SDK at https://pypi.org/project/azure-ai-inference/

from config import Config
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential


# Uncomment the model you want to use - PHI or MISTRAL
# The emphasis here is you can use the same code to interact with different models

model = Config("phi3")
# model = Config("mistral")

# Create the Azure Chat Completions client
# Set default values for the client eg max_tokens. 
# Defaults can be overridden in the complete method
client = ChatCompletionsClient(
    endpoint=model.endpoint,
    credential=AzureKeyCredential(model.key),
    max_tokens=100,
)

# Now get model info
model_info = client.get_model_info()

print(f"Model name: {model_info.model_name}")
print(f"Model provider name: {model_info.model_provider_name}")
print(f"Model type: {model_info.model_type}")


# Create a completion message
response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="How many feet are in a mile?"),
    ],
)

# Print the response
print(response.choices[0].message.content)
