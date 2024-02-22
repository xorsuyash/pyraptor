from sentence_transformers import SentenceTransformer   

model=SentenceTransformer("all_MiniLM-L6-v2")

def embedding(chunks):

    embedding=model.encode(chunks)
    return embedding 

if __name__=="__main__":
    from chunking import TextChunker
    chunks=TextChunker()
    chunks.chunks()
