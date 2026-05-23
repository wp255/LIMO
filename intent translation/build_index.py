import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

KB_DIR = "kb"
INDEX_PATH = "intent_kb.faiss"
META_PATH = "intent_kb_meta.pkl"
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"

def split_text(text, chunk_size=800, overlap=120):
    text = text.strip()
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks

def load_kb_documents(kb_dir):
    docs = []
    for filename in sorted(os.listdir(kb_dir)):
        if not filename.endswith(".md"):
            continue
        path = os.path.join(kb_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        for i, chunk in enumerate(split_text(text)):
            docs.append({"source": filename, "chunk_id": i, "text": chunk})
    return docs

def main():
    docs = load_kb_documents(KB_DIR)
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode([d["text"] for d in docs], normalize_embeddings=True, show_progress_bar=True)
    embeddings = np.asarray(embeddings, dtype="float32")
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(docs, f)
    print(f"Built index with {len(docs)} chunks.")
    print(f"Saved {INDEX_PATH} and {META_PATH}.")

if __name__ == "__main__":
    main()
