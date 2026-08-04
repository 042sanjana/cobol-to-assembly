from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base


class UploadedFile(Base):

    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    filepath = Column(String, nullable=False)

    status = Column(String)

    # One uploaded file can have many modules
    modules = relationship(
        "Module",
        back_populates="uploaded_file",
        cascade="all, delete-orphan"
    )


class Module(Base):

    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to uploaded file
    upload_id = Column(
        Integer,
        ForeignKey("uploaded_files.id"),
        nullable=False
    )

    # Removed unique=True
    module_name = Column(String, nullable=False)

    variables = Column(Text)

    instructions = Column(Text)

    registers = Column(Text)

    dependencies = Column(Text)

    assembly_code = Column(Text)

    cobol_code = Column(Text)

    syntax_report = Column(Text)

    business_rules = Column(Text)

    validation_report = Column(Text)

    execution_status = Column(String)

    uploaded_file = relationship(
        "UploadedFile",
        back_populates="modules"
    )