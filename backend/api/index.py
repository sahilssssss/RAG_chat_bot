from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

# API endpoint to handle user queries
@app.post("/api/ask")
async def ask_question(query: str):
    # Here you should implement the logic to process the query.
    # For now, we'll just return the same query as a response.
    return {"answer": f"Response to: {query}"}

# Lambda handler for Vercel serverless function
handler = Mangum(app)
