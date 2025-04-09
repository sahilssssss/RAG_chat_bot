import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleRetriever:
    def __init__(self):
        self.documents = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.doc_vectors = None

    def fit(self, documents):
        self.documents = documents
        texts = [doc["content"] for doc in documents]
        self.doc_vectors = self.vectorizer.fit_transform(texts)

    def retrieve(self, query, threshold=0.3):
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.doc_vectors).flatten()
        top_idx = similarities.argmax()
        if similarities[top_idx] < threshold:
            return "I don't know"
        return self.documents[top_idx]["content"]

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump((self.documents, self.vectorizer, self.doc_vectors), f)

    def load(self, path):
        with open(path, "rb") as f:
            self.documents, self.vectorizer, self.doc_vectors = pickle.load(f)
