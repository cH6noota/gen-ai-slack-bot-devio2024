import logging
from slack_app import app

@app.error
def handle_error(event, say, error, logger):
    logger.exception(error)
    say(
        channel=event["channel"],
        thread_ts=event["ts"],
        text=f"エラーが発生しました\n{error}"
    )

