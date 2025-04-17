#importing subprocess for calling another file
from subprocess import call





#importing libraries to access llama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
#from contcnt_2_DOCX import create_docx



   
    #template for converation history
template= '''
    Answer the question below.

    Here is the conversation history:{context}

    Question= {question}

    Answer= 

    '''
    #creating an object for calling the model
model=OllamaLLM(model="llama3.1:8b")

    #creating an object for the template
prompt=ChatPromptTemplate.from_template(template)

    #creating the chain
chain= prompt | model

 

'''result=chain.invoke({"context":"","question":"How are you??"})
    print(result)
    while(True):
        i=input("conv :")
        result=model.invoke(input=i)
        print(result)'''





    #fucntion for AI convo
def handle_conversation():
        context=""
        print("Welcome to the conversation! Type 'exit' to end the chat.")
        while True:
            user_input=input("You: ")
            if user_input.lower() == 'exit':
                print("Ending conversation.")
                break
            
            result=chain.invoke({"context":context,"question":user_input})
            print("Bot: ",result)
            context+= f"\nUser: {user_input}\nBot: {result}"
        return context



if __name__ == "__main__":
        doc_content=handle_conversation()
      


import subprocess

subprocess.run(["python","contcnt_2_DOCument.py",doc_content])


