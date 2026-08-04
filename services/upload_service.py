from database.config import SessionLocal
from database.models import UploadedFile


class UploadService:

    def create(self, filename, filepath):

        db = SessionLocal()

        upload = UploadedFile(
            filename=filename,
            filepath=filepath,
            status="Uploaded"
        )

        db.add(upload)
        db.commit()
        db.refresh(upload)

        upload_id = upload.id

        db.close()

        return upload_id

    def update_status(self, upload_id, status):

        db = SessionLocal()

        upload = db.query(UploadedFile).filter(
            UploadedFile.id == upload_id
        ).first()

        if upload:

            upload.status = status

            db.commit()

        db.close()