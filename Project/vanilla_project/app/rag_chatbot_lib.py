from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_models import BedrockChat
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import os


def get_llm():

    model_kwargs = {  # anthropic
        "max_tokens": 512,
        "temperature": 0,
        "top_k": 250,
        "top_p": 1,
        "stop_sequences": ["\n\nHuman:"],
    }

    llm = BedrockChat(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",  # set the foundation model
        model_kwargs=model_kwargs,  # configure the inference parameters
        credentials_profile_name='<default_profile>',
    )

    return llm


def get_retriever():  # creates and returns an in-memory vector store to be used in the application

    # Amazon Bedrock - KnowledgeBase Retriever
    retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id="J9ILKVUWWO",  # 👈 Set your Knowledge base ID
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
        credentials_profile_name='<default_profile>',
    )

    return retriever


def get_memory():  # create memory for this chat session

    memory = ConversationBufferWindowMemory(
        memory_key="chat_history", return_messages=True
    )  # Maintains a history of previous messages

    return memory


def get_rag_chat_response(input_text, memory):  # chat client function

    llm = get_llm()

    retriever = get_retriever()

    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Use three sentence maximum and keep the answer concise. "
        "Context: {context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)

    chat_response = chain.invoke({"input": input_text})

    return chat_response["answer"]
