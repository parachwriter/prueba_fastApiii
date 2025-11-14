from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Integer, ForeignKey, Date
from typing import List, Optional
from datetime import date
from app.db.base import Base

class Vehicle(Base):
    __tablename__ ="vehiculos"

    id: Mapped[int] = mapped_column(primary_key = True, index = True) #podria elimianr el index segun entiendo, pero ya veremos
    brand : Mapped[str] = mapped_column(String(100), nullable= False, index= True)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable= False)
    plate: Mapped[str]= mapped_column(String(10), nullable= False)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable = False)



    ##debería poner algo más aqui?
     