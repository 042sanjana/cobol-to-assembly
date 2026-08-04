import os
import shutil

from services.upload_service import UploadService

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_file(file):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    upload_service = UploadService()

    upload_id = upload_service.create(
        file.filename,
        filepath
    )

    return filepath, upload_id