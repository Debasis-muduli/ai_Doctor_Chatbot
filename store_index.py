from src.helper import load_pdf_file,text_split,download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


extracted_data=load_pdf_file(data='Data/')
text_chunks=text_split(extracted_data)
embeddings = download_hugging_face_embeddings()
# Embed each chunk and upsert the embeddings into your Pinecone index.

try:
    pc = Pinecone(api_key=PINECONE_API_KEY)
    
    index_name = "medibot"
    
    # Check if index already exists
    existing_indexes = pc.list_indexes()
    if index_name in existing_indexes:
        print(f"Index '{index_name}' already exists")
    else:
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        print(f"Successfully created index '{index_name}'")
except Exception as e:
    print(f"Error: {str(e)}")

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)