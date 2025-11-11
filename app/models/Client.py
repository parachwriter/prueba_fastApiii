from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func
from typing import List, Optional
from datetime import datetime

from app.db.base import Base

class Cliente(Base):
    __tablename__ = "cliente"
    id: Mapped[int] = mapped_column(primary_key = True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False,index=True)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20),nullable=True)
    registry_date: Mapped[datetime] = mapped_column(DateTime(timezone = True), server_default= func.now()) 


