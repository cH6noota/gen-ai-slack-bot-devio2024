import sys

manifest_base = """
display_information:
  name: GenAIBOT
features:
  bot_user:
    display_name: gen-ai-bot
    always_online: false
oauth_config:
  scopes:
    bot:
      - app_mentions:read
      - chat:write
settings:
  event_subscriptions:
    request_url: {request_url}
    bot_events:
      - app_mention
  org_deploy_enabled: false
  socket_mode_enabled: false
  token_rotation_enabled: false
"""

if __name__ == "__main__":
    args = sys.argv

    url = args[1].replace(" ","").replace("　","")

    print(
        manifest_base.format(
            request_url=url
        )
    )


