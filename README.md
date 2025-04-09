# Chatbot Application (RAG - Retrieval-Augmented Generation)

LIVE LINK - https://ragchatbot-two.vercel.app/
This is a full-stack chatbot application using FastAPI as the backend and React for the frontend. The chatbot leverages a Retrieval-Augmented Generation (RAG) pipeline for answering user queries from uploaded documents, such as insurance PDFs and support web pages.

## Project Structure

```
chat_app/
├── backend/            # FastAPI backend
│   ├── index.py        # FastAPI app for handling queries
│   ├── requirements.txt # Python dependencies for the backend
├── frontend/           # React frontend
│   ├── src/            # React source code
│   ├── public/         # Public assets
│   ├── package.json    # Frontend dependencies and scripts
└── data/               # Source data (e.g., support PDFs)
```

## Technologies Used

- **Backend**: FastAPI (Python)
- **Frontend**: React (Vite)
- **Deployment**:
  - **Backend**: Render
  - **Frontend**: Vercel

## Setup and Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/yourusername/chatbot.git
cd chatbot
```

### 2. Backend Setup (FastAPI)

**Install Backend Dependencies**

Navigate to the backend/ directory and create a virtual environment:

```
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

Install the required Python dependencies:

```
pip install -r requirements.txt
```

**Run the Backend Locally**

To run the backend locally, use:

```
uvicorn index:app --reload
```

By default, the backend will be running at http://127.0.0.1:8000.

### 3. Frontend Setup (React with Vite)

**Install Frontend Dependencies**

Navigate to the frontend/ directory and install the dependencies:

```
cd frontend
npm install
```

**Run the Frontend Locally**

To start the frontend locally, run:

```
npm run dev
```

The frontend will be available at http://localhost:3000.

## Deployment

### 4. Backend Deployment (Render)

Deploy the backend to Render:

1. Create a Render account at [render.com](https://render.com).
2. Create a new Web Service on Render.
3. Connect your GitHub repository and select the backend folder.
4. Set the build command to `pip install -r requirements.txt` and the start command to `uvicorn index:app --host 0.0.0.0 --port 10000`.
5. Deploy the service.

After deployment, your backend will be available at the Render URL (e.g., https://your-backend-url.onrender.com).

### 5. Frontend Deployment (Vercel)

Deploy the frontend to Vercel:

1. Create a Vercel account at [vercel.com](https://vercel.com).
2. Import your repository and select the frontend/ folder for deployment.
3. Vercel will automatically detect the React app and build it using `npm run build`.
4. Deploy the frontend.

After deployment, your frontend will be available at the Vercel URL (e.g., https://your-frontend-url.vercel.app).

### 6. Connecting Frontend and Backend

In your frontend (App.jsx), update the backend URL in the axios.post() request to the deployed Render URL:

```
const res = await axios.post('https://your-backend-url.onrender.com/ask', new URLSearchParams({ query: input }));
```

Make sure that the `/ask` endpoint is correctly implemented in your FastAPI backend and CORS is properly configured.

## Usage

Once both frontend and backend are deployed:

1. Navigate to the frontend URL (e.g., https://your-frontend-url.vercel.app).
2. Ask a question in the chat interface, and the bot will respond based on the information available in the connected sources (e.g., PDFs and support web pages).

## Troubleshooting

**CORS Issues**: Ensure that CORS is enabled on the backend to allow the frontend to make requests.

In index.py, add:

```
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**404 Errors**: Ensure that the correct backend URL is used in the frontend.

**Deployment Failures**: Check the logs on Render and Vercel for errors in the deployment process.
