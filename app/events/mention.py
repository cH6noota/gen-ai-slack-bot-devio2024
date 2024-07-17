import json
import time
from lib.chat import chat_simple, chat_use_history
from lib.common import preprocessing
from slack_app import app


@app.event("app_mention")
def mention(event, say):
    text = preprocessing(event["text"])
    thread_ts = event.get("thread_ts")

    if thread_ts:
        content = chat_use_history(text, f"{thread_ts}")
    else:
        content = chat_use_history(text, f'{event["ts"]}')

    say(
        channel=event["channel"],
        thread_ts=event["ts"],
        text=content
    )


