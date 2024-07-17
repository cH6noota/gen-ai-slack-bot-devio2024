
import os

from app.lib.common import mention_replace


question = "今は何回目の会話ですか？"

session_id = "hogehoge11"

os.environ["ModelId"] = 'amazon.titan-text-premier-v1:0'
os.environ["ModelRegion"] = 'us-east-1'
os.environ["TableName"] = 'gen-ai-bot-SessionTable-1GKMB4K5LHFKX'
os.environ["KeyName"] = 'sessionId'


from app.lib.chat import chat_start

# for i in range(30):
#     print(chat_start(question, session_id))

text= "<@U079SPLTV0B>\\nTEST"
print(mention_replace(text))