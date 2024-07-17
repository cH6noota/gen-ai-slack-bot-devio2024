import logging, os
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from slack_bolt import App
from lib.secret import get_secret, local_get_secret


SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


localIs = os.environ.get('AWS_SAM_LOCAL')
SECRET_NAME = os.environ.get('SecretName')


if localIs:
    secrets = local_get_secret(SECRET_NAME)
    signing_secret = secrets.get("SIGNING_SECRET")
    token = secrets.get("SLACK_BOT_TOKEN")
    os.environ["ModelId"] = 'amazon.titan-text-premier-v1:0'
    os.environ["ModelRegion"] = 'us-east-1'
    os.environ["TableName"] = 'gen-ai-bot-SessionTable-1GKMB4K5LHFKX'
    os.environ["KeyName"] = 'sessionId'

else:
    secure_tokens = get_secret(SECRET_NAME)
    signing_secret = secure_tokens.get("SIGNING_SECRET")
    token = secure_tokens.get("SLACK_BOT_TOKEN")
    print(signing_secret, token, secure_tokens)



app = App(
    process_before_response=True,
    signing_secret=signing_secret,
    token=token,
)
