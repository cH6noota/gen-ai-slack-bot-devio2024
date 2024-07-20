import os
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import (
    DynamoDBChatMessageHistory,
)




def chat_simple(question):
    chat = ChatBedrock(
        model_id=os.environ.get("ModelId"),
        model_kwargs={"temperature": 0.1},
        region_name=os.environ.get("ModelRegion")
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "あなたはAIアシスタントです。"),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    chain = prompt | chat
    result = chain.invoke(
        {
            "messages": [HumanMessage(content=question)]
        }
    )
    return result.content


def chat_use_history(question, session_id, model_id, system_prompt):
    chat = ChatBedrock(
        model_id=model_id,
        model_kwargs={"temperature": 0.1},
        region_name=os.environ.get("ModelRegion")
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    chat_history = DynamoDBChatMessageHistory(
            table_name=os.environ.get("SessionTable"), 
            primary_key_name=os.environ.get("SessionTableKey"),
            session_id=session_id, 
    )
    # 質問追加
    chat_history.add_user_message(question)

    chain = prompt | chat

    ## chainの実行
    result = chain.invoke(
        {
            "messages": chat_history.messages
        }
    )
    # 回答結果の保存
    chat_history.add_ai_message(result.content)

    return result.content
