import logging, os
from slack_bolt import App
from lib.common import model_list
from lib.secret import get_secret, local_get_secret

SECRET_NAME = os.environ.get('SecretName')

secure_tokens = get_secret(SECRET_NAME)
signing_secret = secure_tokens.get("SIGNING_SECRET")
token = secure_tokens.get("SLACK_BOT_TOKEN")

app = App(
    process_before_response=True,
    signing_secret=signing_secret,
    token=token,
)
