from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for simplicity, but for production, specify your frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins instead of "*"
    allow_credentials=True,
    allow_methods=["*"],  # Or restrict to specific methods like ["GET", "POST"]
    allow_headers=["*"],
)

@app.post("/ask")
def ask(query: str):
    # Your logic here
    return {"response": "This is a response to your query"}
