# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
# app.include_router(bad_words_router, prefix="/api/badWords")

@app.get("/")
def root():
    return {"message": "Welcome to the RedTeam Arena backend!"}