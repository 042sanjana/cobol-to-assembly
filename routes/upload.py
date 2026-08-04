from fastapi import APIRouter, UploadFile, File

from services.file_service import save_file
from services.upload_service import UploadService
from preprocessing.preprocessing import Preprocessor

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    # -----------------------------
    # Save uploaded file
    # -----------------------------
    filepath, upload_id = save_file(file)

    upload_service = UploadService()

    # -----------------------------
    # Update Status
    # -----------------------------
    upload_service.update_status(
        upload_id,
        "Preprocessing"
    )

    # -----------------------------
    # Run Preprocessing
    # -----------------------------
    processor = Preprocessor()

    result = processor.process(
        filepath=filepath,
        upload_id=upload_id
    )

    # -----------------------------
    # Update Status
    # -----------------------------
    upload_service.update_status(
        upload_id,
        "Knowledge Stored"
    )

    # -----------------------------
    # Return Response
    # -----------------------------
    return {
        "upload_id": upload_id,
        "filename": file.filename,
        "path": filepath,
        "message": "Assembly uploaded successfully",
        "analysis": result
    }