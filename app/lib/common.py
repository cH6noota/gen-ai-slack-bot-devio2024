import os
import re
import boto3

def preprocessing(text):
    return re.sub(r'\<@[A-Z0-9]*\>', ' ', text).strip()

def model_list():
    bedrock = boto3.client("bedrock", region_name=os.environ.get("ModelRegion"))
    model_list = bedrock.list_foundation_models()["modelSummaries"]
    model_list = filter(
        lambda model: model["inputModalities"][0]=="TEXT" and model["outputModalities"][0]=="TEXT", 
        model_list
    )
    return [ 
        {
            "ModelId": model["modelId"], 
            # "ModelName": model["modelName"],
        } for model in model_list]

# if __name__ =="__main__":
#     print(model_list())