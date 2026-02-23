from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional

class LoginRequest(BaseModel):
    email:Optional[EmailStr] = None
    phone_number:Optional[str] = None
    password:str

class LoginResponse(BaseModel):
    access_token : str
    refresh_token : str
    token_type : str = 'bearer'

class TokenRefreshRequest(BaseModel):
    refresh_token : str

class TokenRefreshResponse(BaseModel):
    access_token: str
    token_type: str = "bearer" 

class UserOut(BaseModel):
    id: str
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    is_admin: bool
    created_at: datetime
    
    model_config = {"from_attributes": True}

