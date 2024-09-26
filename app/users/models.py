from sqlalchemy import JSON, Column, Computed, ForeignKey, Integer, String, Date
from app.database import Base

class Users(Base):
    __tablename__ = 'users'

    id= Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password= Column(String, nullable=False)