import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('UserTable'))

def get_item(UserId):
    response = table.get_item(Key={
        "UserId":UserId
    })
    return response.get('Item', {
        "UserId":UserId,
        "ModelId":"anthropic.claude-3-haiku-20240307-v1:0",
        "SystemPrompt":"あなたはAIアシスタントです。"
    })


def update_item(UserId, ModelId, SystemPrompt):
    update_expression = "SET #ModelId = :ModelId, #SystemPrompt = :SystemPrompt"
    expression_attribute_names = {
        "#ModelId":"ModelId",
        "#SystemPrompt": "SystemPrompt"
    }
    expression_attribute_values = {
        ":ModelId":ModelId,
        ":SystemPrompt": SystemPrompt
    }
    response = table.update_item(
        Key={
            "UserId":UserId
        },
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )
