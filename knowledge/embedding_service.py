from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


class EmbeddingService:

    def create_embedding(self, text):

        return model.encode(text).tolist()