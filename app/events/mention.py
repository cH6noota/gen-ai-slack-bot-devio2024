import json
import time
from lib.user_db import get_item
from lib.chat import chat_simple, chat_use_history
from lib.common import preprocessing
from slack_app import app


@app.event("app_mention")
def mention(event, say, body):
    user_id = body["user_id"]
    # ユーザ情報の取得
    user_data = get_item(user_id)
    
    text = preprocessing(event["text"])
    thread_ts = event.get("thread_ts")

    if thread_ts:
        content = chat_use_history(text, f"{thread_ts}", user_data["ModelId"], user_data["SystemPrompt"])
    else:
        content = chat_use_history(text, f'{event["ts"]}', user_data["ModelId"], user_data["SystemPrompt"])

    say(
        channel=event["channel"],
        thread_ts=event["ts"],
        text=content
    )


