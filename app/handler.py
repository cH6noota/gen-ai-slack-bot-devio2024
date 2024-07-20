import logging
import json, os
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from slack_bolt import App, Say

SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    header = event["headers"]
    if header.get("X-Slack-Retry-Num"):
        return {
            "statusCode": 200
        }
    
    from slack_app import app
    import events.mention
    import events.error

    slack_handler = SlackRequestHandler(app=app)

    return slack_handler.handle(event, context)


