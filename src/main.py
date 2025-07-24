from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .auth import get_current_user, verify_password, get_password_hash, create_access_token
from .database import get_db, Base, engine
from .models import User, ImageModel
from .schemas import UserCreate, UserOut, Token, ImageOut
from .image_processing import extract_text_from_image, save_image

# FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# API Endpoints
@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/upload-image", response_model=ImageOut)
async def upload_image(file: UploadFile = File(...), current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    # Save file
    unique_filename, file_path = save_image(await file.read(), file.filename)

    # Extract text
    extracted_text = extract_text_from_image(file_path)

    # Save metadata to database
    db_image = ImageModel(
        user_id=current_user.id,
        filename=unique_filename,
        extracted_text=extracted_text
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    return db_image