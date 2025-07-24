import sqlalchemy as sa
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String(50), unique=True, index=True)
    hashed_password = sa.Column(sa.String(255))

class ImageModel(Base):
    __tablename__ = "images"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), index=True)
    filename = sa.Column(sa.String(255))
    upload_date = sa.Column(sa.DateTime, default=sa.func.now())
    extracted_text = sa.Column(sa.Text)