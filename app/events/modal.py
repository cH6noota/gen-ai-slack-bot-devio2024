import json
from slack_app import app
from lib.user_db import update_item

def edit_save(say, logger, body):
    user_id = body["user"]["id"]
    model_id = body["view"]["state"]["values"]["model_id"]["static_select-action"]["selected_option"]["value"]
    system_prompt = body["view"]["state"]["values"]["system_prompt"]["system_prompt"]["value"]
    update_item(user_id, model_id, system_prompt)

def ack_only(ack):
    ack()

app.view("edit_view")(
    ack=ack_only,
    lazy=[edit_save]
)
