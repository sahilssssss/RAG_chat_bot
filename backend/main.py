from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from retriever import SimpleRetriever

app = FastAPI()

# Enable frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

retriever = SimpleRetriever()
retriever.load("knowledge_base.pkl")

@app.post("/ask")
def ask(query: str = Form(...)):
    response = retriever.retrieve(query)
    return {"answer": response}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the chatbot API!"}

@app.post("/ask")
async def ask_question(query: str):
    # Log query and response
    print(f"Query: {query}")
    answer = retriever.get_answer(query)
    print(f"Answer: {answer}")
    return {"answer": answer}

