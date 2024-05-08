import boto3
import json

#Create the connection to Bedrock

bedrock = boto3.client(
    service_name='bedrock',
    region_name='us-west-2'
    
)

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-west-2'
    
)

# List all foundation models
available_models  = bedrock.list_foundation_models()
for model in available_models['modelSummaries']:
    if 'anthropic' in model['modelId']:
        print(model)

