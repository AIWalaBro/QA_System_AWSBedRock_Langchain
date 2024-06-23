# import os
# import sys
# import boto3
# import streamlit as st

# from langchain_community.embeddings import BedrockEmbeddings
# # from langchain.llms.bedrock import Bedrock
# from langchain_community.llms import Bedrock

# from langchain.prompts import PromptTemplate
# from langchain.chains import RetrievalQA
# from langchain_community.vectorstores import FAISS
# # from langchain.vectorstores import FAISS




# from data_ingestion.ingestion import data_ingestion,get_vector_store
# from data_retrieval.retrieval import get_llama2_llm,get_response_llm

# bedrock=boto3.client(service_name="bedrock-runtime")
# bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)

# def main():
#     st.set_page_config("QA with Doc")
#     st.header("QA with Doc using langchain and AWSBedrock")
    
#     user_question=st.text_input("Ask a question from the pdf files")
    
#     with st.sidebar:
#         st.title("update or create the vector store")
#         if st.button("vectors update"):
#             with st.spinner("processing..."):
#                 docs=data_ingestion()
#                 get_vector_store(docs)
#                 st.success("done")
                
#         if st.button("llama model"):
#             with st.spinner("processing..."):
#                 faiss_index=FAISS.load_local("D:\\GenerativeAI_Project_4\\aws\\QA_System_With_AWSBedrock_and_Langchain\\RAG_System_AWSBedRock_ECR_DockerLangchain\\data_ingestion\\faiss_index",bedrock_embeddings,allow_dangerous_deserialization=True)
#                 llm=get_llama2_llm()
                
#                 st.write(get_response_llm(llm,faiss_index,user_question))
#                 st.success("Done")
                
# if __name__=="__main__":
#     #this is my main method
#     main()
    

