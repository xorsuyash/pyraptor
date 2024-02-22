import asyncio
import re

class TextChunker:
    def __init__(self, chunk_size=100):
        self.chunk_size = chunk_size

    def fit(self, text):
        return  self.transform(text)

    def transform(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        current_chunk = ""
        result_chunks = []
        for sentence in sentences:
            if len(current_chunk.split()) + len(sentence.split()) <= self.chunk_size:
                current_chunk += sentence + " "
            else:
                result_chunks.append(current_chunk.strip())
                current_chunk = sentence + " "

        if current_chunk:
            result_chunks.append(current_chunk.strip())

        return result_chunks

    def chunks(self, text):
        return self.transform(text)
    
if __name__=="__main__":

    with open('gameofthrones (2).txt','r') as f:
        text=f.read()
    
    chunks=TextChunker()
    chunks.fit(text)
    print(chunks.chunks(text)[11538])