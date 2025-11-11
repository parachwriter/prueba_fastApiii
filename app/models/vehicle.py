from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date
from typing import List, Optional
from datetime import date
from app.db.base import Base

class Vehicle(Base):
    __tablename__ ="vehiculos"

    id: Mapped