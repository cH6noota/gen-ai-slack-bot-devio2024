def view(user_data, model_id_list):

    options = [
        {
            "text": {
                "type": "plain_text",
                "text": model["ModelId"],
                "emoji": True
            },
            "value": model["ModelId"]
        } for model in model_id_list
    ]
    
    return {
        "type": "modal",
        "callback_id": "edit_view",
        "title": {"type": "plain_text", "text":"ユーザ情報変更"},
        "submit": {"type": "plain_text", "text":"送信"},
        "blocks": [
            {
                "type": "input",
                "block_id": "model_id",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": user_data["ModelId"],
                        "emoji": True
                    },
                    "options": options,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "モデルID",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "system_prompt",
                "label": {"type": "plain_text", "text":"システムプロンプト"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "system_prompt",
                    "multiline":True,
                    "placeholder": {
                        "type": "plain_text",
                        "text": user_data["SystemPrompt"],
                        "emoji": True
                    }
                }
            }
        ]
    }
