
from slack_app import app, model_id_list
from modal.edit_view import view
from lib.user_db import get_item


def edit(body, client, logger, say):
    user_id = body["user_id"]
    # ユーザ情報の取得
    user_data = get_item(user_id)
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=view(user_data, model_id_list)
        )
    except:
        logger.warning("client.views_open Error")
    
def ack_only(ack):
    ack()

app.command("/edit")(
    ack=ack_only,
    lazy=[edit]
)