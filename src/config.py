import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:root@localhost/textron")
SECRET_KEY = os.getenv("SECRET_KEY", "82062f7b0acf0fbd3e070fa2732ce4f1ed7e4a6c67bcb3e2a26a281ddf8b9e82")  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
UPLOAD_DIR = "uploads"

# Create upload directory if it doesn't exist
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)