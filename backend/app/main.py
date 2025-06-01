# calorator-backend/app/main.py

from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(
    title="Calorator API",
    description="AI-powered nutrition analysis for your food items.",
    version="0.1.0",
)

@app.get("/")
async def root():
    """
    Root endpoint for the Calorator API.
    Returns a welcome message and API status.
    """
    return {"message": "Welcome to Calorator API! Go to /docs for API documentation."}

@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Returns a simple status to indicate the API is running.
    """
    return {"status": "ok", "message": "Calorator API is healthy!"}

# You'll add more routes and include routers from your views/ directory later
# Example:
# from app.views import food
# app.include_router(food.router, prefix="/food", tags=["Food Analysis"])