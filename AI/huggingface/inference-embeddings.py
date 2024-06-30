from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.chains import create_retrieval_chain
from langchain_community.llms import HuggingFacePipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
import gradio as gr
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM,pipeline
from langchain_community.embeddings.huggingface import HuggingFaceInferenceAPIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
import os
import torch
prompt = PromptTemplate.from_template("""This is AI generated content:
<context>
{context}
</context>
Question: {input}""")

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xl")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-xl")

#embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
embeddings=HuggingFaceInferenceAPIEmbeddings(model_name="intfloat/multilingual-e5-large-instruct", api_key=os.environ.get("key"))

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
)
llm=HuggingFacePipeline(pipeline=pipe)

loader = TextLoader("data.txt")
docs =loader.load()
text_splitter = SemanticChunker(embeddings)
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

document_chain = create_stuff_documents_chain(llm, prompt)

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

def askAI(message,chat_history):
    response = retrieval_chain.invoke({"input": message})
    return response["answer"]
    
examples = [
    'What is your name?',
    "Where am I from",
]
gr.ChatInterface(
    fn=askAI,
    title ="Ask about me",
    theme='sudeepshouche/minimalist',
    examples=examples
).launch(debug=True,force_download=True)