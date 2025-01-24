# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.badwords import router as bad_words_router
from app.routes.chat import router as chat_router

app = FastAPI()

# CORS configuration for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(bad_words_router, prefix="/api/badWords")
app.include_router(chat_router, prefix="/api/chat")

@app.get("/")
def root():
    return {"message": "Welcome to the RedTeam Arenas backend!"}