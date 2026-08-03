from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import create_database

from routes.upload import router as upload_router

create_database()

app = FastAPI(
    title="Assembly to COBOL Migration"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)


@app.get("/")
def home():

    return {
        "message": "Assembly to COBOL AI Migration"
    }