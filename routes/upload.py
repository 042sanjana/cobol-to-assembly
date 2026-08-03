from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.file_service import save_file
from preprocessing.preprocessing import Preprocessor

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    # Save uploaded Assembly file
    filepath = save_file(file)

    # Run preprocessing
    processor = Preprocessor()
    result = processor.process(filepath)

    # Return upload details + preprocessing analysis
    return {
        "filename": file.filename,
        "path": filepath,
        "message": "Assembly uploaded successfully",
        "analysis": result
    }