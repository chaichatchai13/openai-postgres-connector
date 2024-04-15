from fastapi import FastAPI
from .routes import router
from .database import init_db
from dotenv import load_dotenv
app = FastAPI()

# Include router
app.include_router(router)

# Initialize database tables
@app.on_event("startup")
def startup_event():
    load_dotenv()  # Ensures that your environment variables are loaded
    # Create database tables
    init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
