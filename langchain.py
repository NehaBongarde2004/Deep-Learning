
!pip install --upgrade langchain langchain-core langchain-groq

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


os.environ["GROQ_API_KEY"] = ""


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)


prompt = ChatPromptTemplate.from_template(
    "Answer in a simple and short way:\n{question}"
)


chain = prompt | llm


while True:
    question = input("\nAsk your question (type 'exit' to quit): ").strip()

    if question.lower() == "exit":
        print("Goodbye")
        break

    if not question:
        print("Please enter a valid question")
        continue

    try:
        response = chain.invoke({"question": question})
        print("Answer:", response.content)
    except Exception as e:
        print("ERROR:", e)


