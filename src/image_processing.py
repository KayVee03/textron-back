from fastapi import HTTPException
import os
import pytesseract
from PIL import Image
import uuid
from .config import UPLOAD_DIR

def extract_text_from_image(image_path: str) -> str:
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text extraction failed: {str(e)}")

def save_image(file, filename: str):
    file_extension = filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file)
        return unique_filename, file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")