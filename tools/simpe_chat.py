import os
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


model_id = 'amazon.titan-text-premier-v1:0'
region_name = 'us-east-1'


chat = ChatBedrock(
    model_id=model_id,
    model_kwargs={"temperature": 0.1},
    region_name=region_name
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたはAIアシスタントです。"),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


def chat_simple(question):
    chain = prompt | chat
    result = chain.invoke(
        {
            "messages": [HumanMessage(content=question)]
        }
    )
    return result.content


if __name__ == "__main__":
    question = "今は何回目の会話ですか？"
    print(chat_simple(question))