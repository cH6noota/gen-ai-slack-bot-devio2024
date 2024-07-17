import os, json, boto3
import urllib.request


region_name = os.environ.get("AWS_REGION")
SECRET_NAME = os.environ.get('SecretName')


def get_secret(secret_name):
    secrets_extension_endpoint = "http://localhost:2773/secretsmanager/get?secretId=" + secret_name
    headers = {"X-Aws-Parameters-Secrets-Token": os.environ.get('AWS_SESSION_TOKEN')}
    secrets_extension_req = urllib.request.Request(secrets_extension_endpoint, headers=headers)
    with urllib.request.urlopen(secrets_extension_req) as response:
        secret_config = response.read()
    secret_json = json.loads(secret_config)['SecretString']
    return json.loads(secret_json)


def local_get_secret(secret_name):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    secret_values = get_secret_value_response['SecretString']
    return json.loads(secret_values)

