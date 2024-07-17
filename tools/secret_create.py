import boto3
import json
import sys

args = sys.argv


# AWS Secrets Managerのクライアントを初期化
secretsmanager_client = boto3.client('secretsmanager')

def create_secret(secret_name, description, secret_string):
    try:
        response = secretsmanager_client.create_secret(
            Name=secret_name,
            Description=description,
            SecretString=secret_string
        )
        print(f"Secret '{secret_name}' created successfully.")
        return response
    except Exception as e:
        print(f"Error creating secret: {str(e)}")
        return None




if __name__ == "__main__":
    # シークレットの情報を設定
    secret_name = 'gen-ai-bot-handson'
    description = 'Hands-on generation AI BOT'

    secret = args[1].replace(" ","").replace("　","")
    token = args[2].replace(" ","").replace("　","")

    if "xoxb-" not in token or "xoxb-" in secret:
        raise ValueError, "引数1つ目にはSigning Secret, 引数2つ目にはBot User OAuth Tokenを入力してください"

    secret_string = json.dumps({
        'SIGNING_SECRET': secret,
        'SLACK_BOT_TOKEN': token
    })

    # シークレットを作成
    create_secret(secret_name, description, secret_string)
