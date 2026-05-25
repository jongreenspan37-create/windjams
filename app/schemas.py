
from pydantic import BaseModel, ConfigDict, Field

#inbound
class RegisterUser(BaseModel):
    # Using specific names matching your form fields
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    
    # EmailStr automatically validates that the input is a real email address format
    email: EmailStr = Field(..., max_length=100)
    
    # Plain text password from the form (will be hashed before saving to DB)
    password: str = Field(..., min_length=8, max_length=50)

#outbound
class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    position_id: int
    date_registered: date
    is_active: bool
    is_admin: bool

    # Allows Pydantic to read your SQLAlchemy model instances directly
    model_config = ConfigDict(from_attributes=True)
