import uuid
from datetime import date, datetime, timezone
from typing import List, Optional

from sqlalchemy import String , Text, Date, ForeignKey, text 
from sqlalchemy.dialects.postgresql import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base  



class UserDetails(Base):
    __tablename__="users_details"
    
    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)


    phone_no: Mapped[str] = mapped_column(String(100))
    address_1: Mapped[str] = mapped_column(String(100))
    address_2: Mapped[str] = mapped_column(String(100))
    address_3: Mapped[str] = mapped_column(String(100))
    address_4: Mapped[str] = mapped_column(String(100))

    user: Mapped[Optional["Users"]] = relationship(back_populates="details")

class PositionDetails(Base):
    __tablename__="position_details"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))

    users: Mapped[List["Users"]] = relationship(back_populates="position")
    

class Users(Base):
    __tablename__="users"

    id: Mapped[int] = mapped_column(ForeignKey("user_details"), primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name:  Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    position_id: Mapped[int] = mapped_column(ForeignKey("position_details.id"), default=0, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), required=True)
    date_registered: Mapped[date] =mapped_column(default=lambda: datetime.now(timezone.utc).date())
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, nullable=False)
    
    
    # Relationship to Position table (Many Users to One Position)
    position: Mapped["PositionDetails"] = relationship(back_populates="users")
    details: Mapped["UserDetails"] = relationship(back_populates="user")
    

