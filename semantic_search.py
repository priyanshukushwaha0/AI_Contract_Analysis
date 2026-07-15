from sentence_transformers import SentenceTransformer
import faiss

def build_index(texts):
    model=SentenceTransformer("all-MiniLM-L6-v2")
    emb=model.encode(texts)
    index=faiss.IndexFlatL2(emb.shape[1])
    index.add(emb)
    return model,index