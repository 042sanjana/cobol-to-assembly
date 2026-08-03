from sqlalchemy import Column, Integer, String
from database.config import Base


# Uploaded file table
class UploadedFile(Base):

    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    filepath = Column(String)
    status = Column(String)


# Module table
class Module(Base):

    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)

    module_name = Column(String)

    variables = Column(String)

    dependencies = Column(String)