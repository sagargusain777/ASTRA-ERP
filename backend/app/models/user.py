
from enum import unique
from uuid import uuid4
from sqlalchemy import DateTime , Column ,Integer ,String ,Boolean
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String,primary_key = True , index=True , default = lambda:str(uuid4()))
    email = Column(String,unique = True,nullable = False)
    phone = Column(String,unique = True , nullable = False)
    hashed_password = Column(String,nullable = False)
    is_admin = Column(Boolean,default=False)
    created_at = Column(DateTime(timezone=True) , server_default = func.now())







